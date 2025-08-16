# Synapse trading bot🌀
[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/+pB6j65Kv7cdjZmU0)

<img width="484" height="118" alt="image" src="https://github.com/user-attachments/assets/87a4f93a-1d8d-4aba-86f6-6a2ce2b18ebf" />



# Descritpiton
**Synapse is an open-source intelligent trading bot designed to generate trading signals by leveraging live market data, social media sentiment, and historical patterns. It features multiple modes of operation, backtesting, an AI-powered engine, and seamless integration with Telegram for real-time monitoring and control.**

# Main Features
- Automatically generates trading signals based on real-time market conditions, executes buy/sell orders using those signals(optional), and sets optimal stop-loss and take-profit levels.
           
- Backtesting Support: Simulate your own or the bot’s trading strategy on historical market data to evaluate performance, fine-tune parameters, and optimize results—without risking real capital.
           
- Self-Training: Synapse continuously learns from the user’s trading results, adapting its strategies and enhancing its overall intelligence over time. With each update, we also train Synapse.

- **Your** Strategy Optimization: Synapse analyzes your custom trading strategy using machine learning and market data, then suggests targeted improvements.

- Simple Interface and configuration: Intuitive control via Telegram bot or web UI.

- Manual mode: Snipe selected tokens at optimal price , define preferred stop-loss and take-profit levels, and apply their own custom trading strategies for complete control and precision.

- Notifications: The bot keeps you informed throughout the trading process with real-time updates via Telegram.

- Price-predicton: Synapse forecasts individual token prices by analyzing current market trends, the Fear and Greed Index, and historical price patterns.

- Financial Management: Synapse monitors your overall trading performance, tracking cumulative profit and loss in real time. Before initiating any trade, it alerts you to potential risks.



# Supported exchanges📊
<div align="center">
<img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/90d8ca5a-71d8-404d-80a4-578e1efe2db9" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/900cb4eb-8d14-4b51-97b1-3c515ea60141" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/cdc3f7ef-6ad4-423c-b0bc-8669761774db" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/faec88fc-4946-48e7-b98f-157e2234e7f8" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/0f836b8b-5f4b-4ddb-a1d2-7318d883d51f" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/29df4163-dd45-42ff-96dc-aec0e5d1788a" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/8c1e6327-f80d-42a7-a918-5fd5c4daf441" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/f4008a15-a371-4bc5-9ca0-95839eb2afbf" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/eaafbfe9-1359-4068-a321-b4d982739edf" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/492b1317-cbdf-4a17-b67e-eebbe47a4315" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/31fbf32d-dfbb-4bd8-b10d-782c6fc3a74f" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/9b61064c-e4a7-4458-9331-c04c746cf5b8" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/c9b41a39-344d-4163-84b5-d281c1c5c9a2" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/b21dddf6-5787-4da0-a2d9-440e91f71dd2" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/73741faf-0aa5-4967-bbea-ec101da6b9d2" />  <img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/2af7c9c2-5bf1-4770-accd-785e87c1fb51" />
















 </div>

# Installation 
**Requirements**:
- Python 3.10+
- Git
- Pip
- 2v CPU, 2GB DDR4, 2GB disk space

**To install the bot, follow the steps below**:
```shell
git clone https://github.com/anthugeist/synapse-bot
cd synapse-trading-bot
run.bat
```
 **OR**
 ```shell
git clone https://github.com/anthugeist/synapse-bot
cd synapse-trading-bot
pip install -r requirements.txt
python bot.py
```
To connect Synapse to telegram bot:
1. Put your bot token and chat id in **config.json**
2.
 ```shell
cd synapse-trading-bot
python bot.py --telegram
```
3. To control the bot via Telegram use RPC commands:


| Command | Description |
|----------------------------|:-------------------------------------------------------------------------------------------------------------:|
| `/start`     | Start the bot |       
| `/stop`               | Stop the bot |
| `/stats`              |  Show statistics of your account(balance, trade history, overall profit) |
| `/mode` | Switch trading mode |
|`/status` | Show current operating mode |
| `/autotrade_on` | Enable automatic trading based on generated signals |
| `/autotrade_off` | Disable auto trading |
| `/snipe TOKEN` | Buy selected token instantly at market price or snipe desired price |
| `/sell TOKEN` | Sell selected token instantly at market price |
| `/strategy_suggest` | AI-analyzed strategy recommendations based on your performance |
| `/backtest *strategy name*` | Run backtesting simulation for a saved strategy |
| `/help` | Show full list of commands |

*This is not the full list of RPC commands. To view the complete list, type /help in the bot.*

# Disclaimer
Use the bot at your own risk. I assume for responsibility of your trading results and consequences of using the software. Dont risk the money which you afraid to lose. Be wise.

# Support

***Help/bug reports***

If you have any difficulties or encountered bugs, please join our telegram [community](https://t.me/+9j5RcKMfT5s4M2Q0)

If you have any ideas on how to improve the bot, feel free to contact me on [Telegram](https://t.me/@Hhubbinmo3)

***Buy me a coffee***

If you want to leave me a tip, my bitcoin address is `bc1q3zykl6k0jyk864kdeqdfq6hudfr3ry8wksrr6u`


**Don't forget to put stars!** ⭐













