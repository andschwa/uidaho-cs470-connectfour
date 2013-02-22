class Player:
    def __init__(self, color, interface=None):
        self.color = color
        self.interface = interface

    def getMove(self):
        raise NotImplementedError

class Computer(Player):
    def getMove(self):
        raise NotImplementedError

class Human(Player):
    def getMove(self):
        return self.interface.askMove(self.color)
