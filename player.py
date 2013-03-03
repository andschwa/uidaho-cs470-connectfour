from algorithms import Minimax


class Player:
    def __init__(self, color, interface):
        self.color = color
        self.interface = interface

    def get_move(self, board=None):
        raise NotImplementedError


class Computer(Player):
    def __init__(self, color, interface, difficulty=10):
        super().__init__(color, interface)
        self.difficulty = difficulty

    def get_move(self, board):
        algorithm = Minimax(board)
        move, value = algorithm.best_most(self.color, self.difficulty)
        return move


class Human(Player):
    def __init__(self, color, interface):
        super().__init__(color, interface)

    def get_move(self, board=None):
        return self.interface.ask_move(self.color)
