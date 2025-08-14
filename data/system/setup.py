import asyncio
import aiohttp
from datetime import datetime

from utils.logger import log
from api.gifts import GiftsApi
from db.models import Gift, AutoBuySettings, User, Transaction
from db.session import get_db_session


async def process_gift_purchase(db, gifts_api, user, settings, gift):
    """
    Process the purchase of a single gift for a user.

    Args:
        db: Database session
        gifts_api: API client for gift transactions
        user: User object
        settings: Auto-buy settings for the user
        gift: Gift object

    Workflow:
        1. Validate price and supply constraints
        2. Check user balance
        3. Attempt to send the gift via API
        4. Update database records if successful
    """
    gift_price = gift.price
    total_count = gift.total_count
    price_limit_from = settings.price_limit_from
    price_limit_to = settings.price_limit_to
    supply_limit = settings.supply_limit

    if (
        gift_price is not None and
        total_count is not None and
        price_limit_from <= gift_price <= price_limit_to and
        (supply_limit is None or total_count <= supply_limit) and
        user.balance >= gift_price
    ):
        success = await gifts_api.send_gift(
            user_id=user.user_id,
            gift_id=gift.gift_id,
            pay_for_upgrade=False
        )
        if success:
            log.info(
                f"Gift {gift.gift_id} successfully sent to user {user.user_id}."
            )
            user.balance -= gift_price  # Update user balance
            new_transaction = Transaction(
                user_id=user.user_id,
                amount=-gift_price,  # Deduct balance
                telegram_payment_charge_id="buy_gift_transaction",
                payload=f"Autobuy_of_gift_{gift.gift_id}",
                status="completed",
                time=datetime.utcnow().isoformat(),
            )
            db.add(new_transaction)
            return True
        else:
            log.warning(
                f"Failed to send gift {gift.gift_id} to user {user.user_id}."
            )
    else:
        log.info(
            f"Conditions not met for purchasing gift {gift.gift_id} for user {user.user_id}."
        )
    return False


async def start_gift_parsing_loop():
    """
    Continuously parse new gifts and automatically process purchases for eligible users.

    Workflow:
        1. Retrieve the latest available gifts
        2. Update or create gift records in the database
        3. Fetch users with auto-purchase enabled
        4. Process purchases based on user settings
        5. Commit changes and reset new gift flags

    Args:
        None
    """
    gifts_api = GiftsApi()
    # Use a single session with a timeout for the entire execution loop
    session_timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        while True:
            try:
                # Retrieve the list of available gifts via API
                gifts = await gifts_api.aio_get_available_gifts(session)
                if not gifts:
                    log.warning(
                        "Gift list is empty or an error occurred while retrieving data."
                    )
                    await asyncio.sleep(10)
                    continue

                with get_db_session() as db:
                    # Update or create gift records in the database
                    for gift in gifts:
                        existing_gift = db.query(Gift).filter(
                            Gift.gift_id == gift['id']).first()
                        if existing_gift:
                            updated = False
                            if existing_gift.price != gift.get('star_count', 0):
                                existing_gift.price = gift.get('star_count', 0)
                                updated = True
                            if existing_gift.remaining_count != gift.get('remaining_count'):
                                existing_gift.remaining_count = gift.get(
                                    'remaining_count')
                                updated = True
                            if existing_gift.total_count != gift.get('total_count'):
                                existing_gift.total_count = gift.get(
                                    'total_count')
                                updated = True

                            if updated:
                                log.info(
                                    f"Updated gift data {existing_gift.gift_id}: "
                                    f"price={existing_gift.price}, remaining={existing_gift.remaining_count}, "
                                    f"total={existing_gift.total_count}."
                                )
                        else:
                            new_gift = Gift(
                                gift_id=gift['id'],
                                price=gift.get('star_count', 0),
                                remaining_count=gift.get('remaining_count'),
                                total_count=gift.get('total_count'),
                                is_new=True
                            )
                            db.add(new_gift)
                            log.info(
                                f"Added new gift: {new_gift.gift_id}")

                    db.commit()
                    log.info("Gift list successfully updated in the database.")

                    # Retrieve users with auto-purchase enabled
                    auto_buy_users = db.query(AutoBuySettings).filter(
                        AutoBuySettings.status == "enabled"
                    ).all()
                    # Retrieve the list of newly added gifts for processing
                    new_gifts = db.query(Gift).filter(Gift.is_new == 1).all()

                    for settings in auto_buy_users:
                        user = db.query(User).filter(
                            User.user_id == settings.user_id).first()
                        if not user:
                            continue

                        for cycle in range(settings.cycles):
                            log.debug(
                                f"Cycle {cycle + 1}/{settings.cycles} for user {user.user_id}."
                            )
                            for gift in new_gifts:
                                if user.balance < gift.price:
                                    log.info(
                                        f"Insufficient funds for user {user.user_id} to purchase gift {gift.gift_id}."
                                    )
                                    continue

                                purchase_success = await process_gift_purchase(db, gifts_api, user, settings, gift)
                                if purchase_success:
                                    db.commit()  # Commit changes after a successful purchase

                    # Reset the 'is_new' flag after processing new gifts
                    for gift in new_gifts:
                        gift.is_new = 0
                    db.commit()

                await asyncio.sleep(3)
            except Exception as e:
                log.error(f"Error in the gift parsing process: {e}")
                await asyncio.sleep(3)
