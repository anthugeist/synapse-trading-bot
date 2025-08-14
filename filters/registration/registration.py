#!/usr/bin/env python
# pylint: skip-file 
import pathlib

REPO_ROOT = pathlib.Path(__name__).resolve().parent
SUPPORTED_COIN_LIST = REPO_ROOT / "supported_coin_list"


def sort():
    in_contents = SUPPORTED_COIN_LIST.read_text()
    out_contents = ""
    out_contents += "\n".join(sorted(line.upper() for line in in_contents.splitlines()))
    out_contents += "\n"
    if in_contents != out_contents:
        SUPPORTED_COIN_LIST.write_text(out_contents)


if __name__ == "__main__":
    sort()
