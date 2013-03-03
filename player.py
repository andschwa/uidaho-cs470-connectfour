import random


class Player:
    def __init__(self, color, interface):
        self.color = color
        self.interface = interface

    def get_move(self, board=None):
        raise NotImplementedError


class Computer(Player):
    def __init__(self, color, interface):
        super().__init__(color, interface)

    def get_move(self, board):
        return random.randint(0, board.width)


class Human(Player):
    def __init__(self, color, interface):
        super().__init__(color, interface)

    def get_move(self, board=None):
        return self.interface.ask_move(self.color)
