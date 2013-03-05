from algorithms import Minimax


class Player:
    def __init__(self, color, colors, interface):
        self.color = color
        self.colors = colors
        self.interface = interface

    def get_move(self, board=None):
        raise NotImplementedError


class Computer(Player):
    def __init__(self, color, colors, interface, difficulty=1000):
        super().__init__(color, colors, interface)
        self.difficulty = difficulty

    def get_move(self, board):
        algorithm = Minimax(board, self.colors)
        move, value = algorithm.best_move(self.color, self.difficulty)
        if move is None:
            self.interface.resign(self.color)
        self.interface.announce_move(self.color, move)
        return move


class Human(Player):
    def __init__(self, color, colors, interface):
        super().__init__(color, colors, interface)

    def get_move(self, board=None):
        return self.interface.ask_move(self.color)
