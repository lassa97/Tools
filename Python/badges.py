#!/usr/bin/env python3

import argparse
import requests
import subprocess
import sys

parser = argparse.ArgumentParser(description="A script to create badges fot GitHub via CLI")
parser.add_argument("label", nargs="?", type=str, default="")
parser.add_argument("message", nargs="?", type=str, default="")
parser.add_argument("color", type=str, default="")
parser.add_argument("-s", "--style", type=str, help="Choose a style: plastic | flat | flat-square | for-the-badge | social", default=argparse.SUPPRESS)
parser.add_argument("-l", "--logo", type=str, help="Choose one logo from https://simpleicons.org/", default=argparse.SUPPRESS)
parser.add_argument("-lc", "--logoColor", type=str, help="Choose a color for the logo", default=argparse.SUPPRESS)
parser.add_argument("-lw", "--logoWidth", type=str, help="Choose the width of the logo", default=argparse.SUPPRESS)
parser.add_argument("-lac", "--labelColor", type=str, help="Choose a color for the label", default=argparse.SUPPRESS)
args = parser.parse_args()


ENDPOINT = "https://img.shields.io/badge/"

if args.color == "":
    parser.print_help()
else:
    if len(sys.argv) == 3:
        petition = petition
        response = requests.get(petition)
        if response.status_code == 404:
            print("Something went wrong")
        else:
            subprocess.run(["sensible-browser", petition])
    else:
        petition = "{ENDPOINT}{LABEL}-{MESSAGE}-{COLOR}?".format(ENDPOINT=ENDPOINT, LABEL=args.label, MESSAGE=args.message, COLOR=args.color)
        for arg in vars(args):
            if (arg is not "label") and (arg is not "message") and (arg is not "color"):
                petition += "{PARAM}={VALUE}&".format(PARAM=arg, VALUE=args.__getattribute__(arg))

        petition = petition[:-1]
        response = requests.get(petition)
        if response.status_code == 404:
            print("Something went wrong")
        else:
            subprocess.run(["sensible-browser", petition])