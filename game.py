from random import choice

from board import Board
from error import *
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
            self.players.append(eval(player)(self._getColor(), self.interface))

    def _getColor(self):
        if not self.players:
            return choice(self.colors)
        else:
            colors = list(self.colors)
            colors.remove(self.players[0].color)
            return colors[0]

    def _move(self, player, board):
        try:
            column = player.getMove(board)
            move = self.board.makeMove(column, player.color)
        except InvalidMoveError:
            return None
        return move

    def play(self):
        self.interface.newGame(self.players, self.board)
        while self.playing:
            for player in self.players:
                move = None
                while move is None:
                    move = self._move(player, self.board)
                self.board.printBoard()
                if self.board.playerWon(player.color):
                    self.winner = player
                    self.playing = False
                    break
                if self.board.isFull():
                    self.winner = None
                    self.playing = False
                    break
        self.interface.endGame(self.winner, self.board)
