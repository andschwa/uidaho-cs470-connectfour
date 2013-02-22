#!/usr/bin/python3

import argparse
import sys

import game
import interface

def eatargs():
    parser = argparse.ArgumentParser(description='Play Connect Four!')
    parser.add_argument('--versus', dest='players', action='store_const',
            const=['human', 'human'], help='Play as two humans!')
    parser.add_argument('--solo', dest='players', action='store_const',
            const=['human', 'computer'], help='Play as two humans!')
    parser.add_argument('--auto', dest='players', action='store_const',
            const=['computer', 'computer'], help='Play as two computers!')

def main():
    options, args = eatargs()

    try:
        the_interface = interface.gui()
    except:
        the_interface = interface.cli()

    the_game = game(the_interface, options.players)

    the_game.setup()
    the_game.play()

if __name__ = '__main__':
    sys.exit(main())
