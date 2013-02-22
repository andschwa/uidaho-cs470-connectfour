class Player:
    def __init__(self, color, interface=None):
        self.color = color
        self.interface = interface

    def getmove(self):
        raise NotImplementedError

class Computer(Player):
    def getmove(self):
        raise NotImplementedError

class Human(Player):
    def getmove(self):
        raise NotImplementedError
        self.interface.printBoard()
        #return self.interface.askMove()
