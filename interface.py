import sys

from error import *

class Interface:
    def __init__(self):
        pass
    def printBoard(self):
        raise NotImplementedError
    def askMove(self):
        raise NotImplementedError

class GUI(Interface):
    def __init__(self):
        raise NotImplementedError

class CLI(Interface):
    def __init__(self):
        self.ask_string = "Player {}, in which column would you like to play? "

    def printBoard(self, the_board):
        for row in range(the_board.height-1, -1, -1):
            print('|', end='')
            for column in range(the_board.width):
                space = the_board.board[column][row]
                if space == 'red':
                    print('#', end='')
                if space == 'black':
                    print('*', end='')
                if space is None:
                    print(' ', end='')
                print('|', end='')
            print()

    def askMove(self, color):
        input_ = input(self.ask_string.format(color))
        if input_ == 'exit':
            sys.exit(0)
        try:
            return int(input_)
        except:
            raise InvalidMoveError
