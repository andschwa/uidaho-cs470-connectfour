import argparse
import sys

import error


class Interface:
    def __init__(self, colors):
        self.colors = colors
        self.options = self.eat_args()

    def eat_args(self):
        parser = argparse.ArgumentParser(description='Play Connect Four!')
        parser.add_argument(
            '--versus', dest='players', action='store_const',
            const=['Human', 'Human'], help='Play as two Humans!')
        parser.add_argument(
            '--solo', dest='players', action='store_const',
            const=['Human', 'Computer'], help='Play as two Humans!')
        parser.add_argument(
            '--auto', dest='players', action='store_const',
            const=['Computer', 'Computer'], help='Play as two Computers!')
        return parser.parse_args()

    def print_board(self):
        raise NotImplementedError

    def ask_move(self):
        raise NotImplementedError


class GUI(Interface):
    def __init__(self, colors):
        raise NotImplementedError


class CLI(Interface):
    def __init__(self, colors):
        super().__init__(colors)
        self.ask_string = "Player {}, in which column would you like to play? "

    def get_players(self):
        players = self.options.players
        if players is None:
            players = ['Human', 'Human']
        return players

    def _get_symbol(self, color):
        if color == self.colors[0]:
            return 'O'
        if color == self.colors[1]:
            return 'X'

    def _ask_first(self, players):
        color_string = "Which player shall go first: {} or {}? "
        try:
            input_ = input(color_string.format(
                players[0].color, players[1].color))
        except KeyboardInterrupt:
            self._exit()
        if input_ == 'exit':
            self._exit()
        for player in players:
            if input_ == player.color:
                return player
        if input_ is '':
            return players[0]
        return None

    def new_game(self, players, board):
        welcome_string = "Welcome players: {} is '{}', and {} is '{}'."
        print(welcome_string.format(
            players[0].color, self._get_symbol(players[0].color),
            players[1].color, self._get_symbol(players[1].color)))
        board.print_board()
        print('Your columns are 0 to 6, left to right.')
        first_player = None
        while first_player is None:
            first_player = self._ask_first(players)
        return first_player

    def end_game(self, winner, board):
        if winner is None:
            print('It was a draw!')
        else:
            print('Player {} won!'.format(winner.color))
        board.print_board()

    def print_board(self, the_board):
        print()
        for row in range(the_board.height-1, -1, -1):
            print('|', end='')
            for column in range(the_board.width):
                space = the_board.board[column][row]
                if space == self.colors[0]:
                    print(self._get_symbol(self.colors[0]), end='')
                if space == self.colors[1]:
                    print(self._get_symbol(self.colors[1]), end='')
                if space is None:
                    print(' ', end='')
                print('|', end='')
            print()
        print('|' + '|'.join(str(i) for i in range(the_board.width)) + '|')
        print()

    def _exit(self):
            print('Goodbye cruel world.')
            sys.exit(0)

    def ask_move(self, color):
        try:
            input_ = input(self.ask_string.format(color))
        except KeyboardInterrupt:
            self._exit()
        print()
        if input_ == 'exit':
            self._exit()
        try:
            return int(input_)
        except:
            raise error.InvalidMoveError
