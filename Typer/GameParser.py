import argparse

def game_parser():
    parser = argparse.ArgumentParser(
            prog="AnsiTyper",
            usage="%(prog)s [options]",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description="Simple WPM counter")

    parser.add_argument(
            '-v','--version',
            action='version',
            version="""
%(prog)s v1.0.0
Copyright (C) 2023 Sivefunc
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by a human""")

    parser.add_argument(
            "-w", '--words', 
            type=int,
            help='number of words to type',
            default=30,
            metavar='')

    args = parser.parse_args()
    return args
