from board import Board
from error import *
from player import Human, Computer

class Game:
    def __init__(self, interface, players):
        self.interface = interface
        self.playing = True
        self.winner = None
        self.board = Board(self.interface)

        self.players = [
                Human('red', self.interface),
                Human('black', self.interface)]

    def newGame(self):
        raise NotImplementedError

    def _move(self, player):
        try:
            column = player.getMove()
            move = self.board.makeMove(column, player.color)
        except InvalidMoveError:
            return None
        return move

    def play(self):
        self.board.printBoard()
        while self.playing:
            for player in self.players:
                move = None
                while move is None:
                    move = self._move(player)
                self.board.printBoard()
                if self.board.playerWon(player.color):
                    self.winner = player
                    self.playing = False
                    break
        self.endGame()

    def endGame(self):
        print('Player {} won!'.format(self.winner.color))
        self.board.printBoard()

