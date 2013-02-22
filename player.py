class Player:
    def __init__(self, color, interface):
        self.color = color
        self.interface = interface

    def getMove(self):
        raise NotImplementedError

class Computer(Player):
    def __init__(self, color, interface):
        super().__init__(color, interface)
        raise NotImplementedError

    def getMove(self):
        raise NotImplementedError

class Human(Player):
    def __init__(self, color, interface):
        super().__init__(color, interface)
    def getMove(self):
        return self.interface.askMove(self.color)
