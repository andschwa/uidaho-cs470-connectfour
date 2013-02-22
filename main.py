#!/usr/local/bin/python3

import argparse
import sys

import interface

from error import *
from game import Game


def eatargs():
    parser = argparse.ArgumentParser(description='Play Connect Four!')
    parser.add_argument('--versus', dest='players', action='store_const',
            const=['Human', 'Human'], help='Play as two Humans!')
    parser.add_argument('--solo', dest='players', action='store_const',
            const=['Human', 'Computer'], help='Play as two Humans!')
    parser.add_argument('--auto', dest='players', action='store_const',
            const=['Computer', 'Computer'], help='Play as two Computers!')
    options = parser.parse_args()
    return options

def main():
    options = eatargs()
    players = options.players
    if players is None:
        players = ['Human', 'Human']
    colors = ('red', 'black')

    try:
        the_interface = interface.GUI(colors)
    except NotImplementedError:
        the_interface = interface.CLI(colors)

    the_game = Game(the_interface, colors, players)

    the_game.play()

if __name__ == '__main__':
    sys.exit(main())
