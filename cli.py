import sys
import argparse

parser = argparse.ArgumentParser(description="Convert Markdown to HTML.")
parser.add_argument("-n", "--nav", dest="nav", help="Add a JSON file to use for navigation menu")
parser.add_argument("files", nargs=argparse.REMAINDER, help="Files to be converted to HTML")