#!/usr/bin/env python3

import argparse
import json
import os

# ENDPOINT = "https://raw.githubusercontent.com/github/gemoji/master/db/emoji.json"

FILE = "{HOME}/{FOLDERS}/{FILE}".format(HOME=os.getenv("HOME"), FOLDERS="/Tools/Python", FILE="emojis.json")

# TODO: Autoupdate the file of the emojis

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
  with open(FILE) as file:
    emojis_db = json.loads(file.read())

  emojis = {}

  for emoji in emojis_db:
    if (emoji_name in emoji['names']) or (emoji_name in emoji['tags']):
        emojis.update({emoji['emoji']: emoji['description']})

  if len(emojis) != 0:
    for emoji in emojis:
        print("{EMOJI}: {DESCRIPTION}".format(EMOJI=emoji, DESCRIPTION=emojis[emoji]))
  else:
    print("❌ No emoji found 😿")
  
else:
  emoji_name = args.emoji
  with open(FILE) as file:
    emojis_db = json.loads(file.read())

  emojis = {}

  for emoji in emojis_db:
    name_exists = any(emoji_name in tmp for tmp in emoji['names'])
    tag_exists = any(emoji_name in tmp for tmp in emoji['tags'])
    if name_exists or tag_exists:
      emojis.update({emoji['emoji']: emoji['description']})

    if len(emojis) == args.limit:
      break

  if len(emojis) != 0:
    for emoji in emojis:
      print("{EMOJI}: {DESCRIPTION}".format(EMOJI=emoji, DESCRIPTION=emojis[emoji]))
  else:
    print("❌ No emoji found 😿")
