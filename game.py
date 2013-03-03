from random import choice

import error

from board import Board
from player import Human, Computer


class Game:
    def __init__(self, interface, colors, player_types):
        self.interface = interface
        self.playing = True
        self.winner = None
        self.colors = colors
        self.board = Board(self.interface)
        self.players = []
        for player in player_types:
            self.players.append(
                eval(player)(self._get_color(), self.interface))

    def _get_color(self):
        if not self.players:
            return choice(self.colors)
        else:
            colors = list(self.colors)
            colors.remove(self.players[0].color)
            return colors[0]

    def _move(self, player, board):
        try:
            column = player.get_move(board)
            move = self.board.make_move(column, player.color)
        except error.InvalidMoveError:
            return None
        return move

    def play(self):
        self.interface.new_game(self.players, self.board)
        while self.playing:
            for player in self.players:
                move = None
                while move is None:
                    move = self._move(player, self.board)
                self.board.print_board()
                if self.board.player_won(player.color):
                    self.winner = player
                    self.playing = False
                    break
                if self.board.is_full():
                    self.winner = None
                    self.playing = False
                    break
        self.interface.end_game(self.winner, self.board)
