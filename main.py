#!/usr/local/bin/python3

import sys

import interface

from error import *
from game import Game



def main():
    colors = ('red', 'black')

    try:
        the_interface = interface.GUI(colors)
    except NotImplementedError:
        the_interface = interface.CLI(colors)

    players = the_interface.getPlayers()

    the_game = Game(the_interface, colors, players)

    the_game.play()

if __name__ == '__main__':
    sys.exit(main())
