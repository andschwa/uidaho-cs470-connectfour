#!/usr/local/bin/python3

import argparse
import sys

import interface

from error import *
from game import Game


def eatargs():
    parser = argparse.ArgumentParser(description='Play Connect Four!')
    parser.add_argument('--versus', dest='players', action='store_const',
            const=['human', 'human'], help='Play as two humans!')
    parser.add_argument('--solo', dest='players', action='store_const',
            const=['human', 'computer'], help='Play as two humans!')
    parser.add_argument('--auto', dest='players', action='store_const',
            const=['computer', 'computer'], help='Play as two computers!')
    return parser

def main():
    options = eatargs().parse_args()

    try:
        the_interface = interface.GUI()
    except:
        the_interface = interface.CLI()

    the_game = Game(the_interface, options.players)

    the_game.play()

if __name__ == '__main__':
    sys.exit(main())
