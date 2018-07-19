#!/usr/local/bin/python3.6
# -*-coding:Utf-8 -*

import sys
import argparse

print(sys.argv)

parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="le nb a mettre au carré")
parser.add_argument("-v", "--verbose", action="store_true",\
        help="augmente la verbosité")
args = parser.parse_args()
if args.verbose:
    print("{} ^ 2 = {}".format(args.x, args.x ** 2))
else:
    print(args.x ** 2)
