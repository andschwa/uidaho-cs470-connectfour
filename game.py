import board.Board as Board
import player.Human as Human
import player.Computer as Computer

class Game:
    def __init__(interface, players):
        self.interface = interface
        self.playing = True
        self.board = Board()

        self.players = [
                Human('red', self.interface),
                Human('black', self.interface)]

    def play():
        while self.playing:
            for player in players:
                move = player.getMove()
                self.board.makeMove(move)

