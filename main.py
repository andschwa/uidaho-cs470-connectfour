#!/usr/bin/python3

import argparse
import sys

import game
import interface

def eatargs():
    parser = argparse

def main():
    options, args = eatargs()

    try:
        the_interface = interface.gui()
    except:
        the_interface = interface.cli()

    the_game = game(the_interface, options.players)

if __name__ = '__main__':
    sys.exit(main())
