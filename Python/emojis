#!/usr/bin/env python3

import argparse
import json
import requests

parser = argparse.ArgumentParser(description="A simple emojipedia 📚 for the CLI 💻 made by @lassa97 👨", 
                                usage="%(prog)s [options] emoji", 
                                add_help=False
                                )
parser.add_argument("emoji", nargs="?", type=str, default="beer")
parser.add_argument("-h", "--help", action="help", help="show this help message and exit ❓")
parser.add_argument("-l", "--limit", type=int, help="limit the amount of emojis to display 🔟", default=10)
parser.add_argument("-m", "--match", help="search must match the name of the emoji 🔍", action="store_true")
parser.add_argument("-v", "--version", action="version", help="show program's version number and exit 🏷️", version="%(prog)s 1.0")
args = parser.parse_args()

if args.emoji is "beer":
    parser.print_help()
elif args.match:
    emoji_name = args.emoji
    response = requests.get("https://raw.githubusercontent.com/Olyno/emojis-list/master/emojis.json")
    emojis_db = json.loads(response.text)
    emojis = {}

    for emoji in emojis_db:
        if ":{NAME}:".format(NAME=emoji_name) in emoji['shortNames']:
            emojis.update({emoji['emoji']: emoji['shortNames'][emoji['shortNames'].index(":{NAME}:".format(NAME=emoji_name))]})
            break

    if len(emojis) != 0:
        print("{EMOJI} - {NAME}".format(EMOJI=next(iter(emojis)), NAME=emojis[next(iter(emojis))]))
    else:
        print("❌ No emoji found 😿")
else:
    emoji_name = args.emoji
    response = requests.get("https://raw.githubusercontent.com/Olyno/emojis-list/master/emojis.json")
    emojis_db = json.loads(response.text)
    emojis = {}

    for emoji in emojis_db:
        exists = any(emoji_name in tmp for tmp in emoji['shortNames'])
        if exists:
            emojis.update({emoji['emoji']: emoji['shortNames'][0]})
        if len(emojis) == args.limit:
            break

    if len(emojis) != 0:
        for emoji in emojis:
            print("{EMOJI} - {NAME}".format(EMOJI=emoji, NAME=emojis[emoji]))
    else:
        print("❌ No emoji found 😿")