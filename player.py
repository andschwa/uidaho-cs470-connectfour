import random

class Player:
    def __init__(self, color, interface):
        self.color = color
        self.interface = interface

    def getMove(self, board=None):
        raise NotImplementedError

class Computer(Player):
    def __init__(self, color, interface):
        super().__init__(color, interface)

    def getMove(self, board):
        return random.randint(0, board.width)

class Human(Player):
    def __init__(self, color, interface):
        super().__init__(color, interface)
    def getMove(self, board=None):
        return self.interface.askMove(self.color)
