from error import *

class Board:
    def __init__(self, interface, width=7, height=6):
        self.board = []
        self.width = width
        self.height = height
        self.interface = interface
        for _ in range(self.width):
            self.board.append([None] * self.height)

    def makeMove(self, column, color):
        if column >= self.width:
            raise InvalidMoveError
        row = self._nextLowest(column)
        if self.board[column][row] is not None:
            raise InvalidMoveError
        self.board[column][row] = color
        return (column, row)

    def _nextLowest(self, column):
        for index, value in enumerate(self.board[column]):
            if value is None:
                return index
        raise InvalidMoveError

    def playerWon(self, color):
        # horizontal
        for x in range(self.width - 3):
            for y in range(self.height):
                if self.board[x][y] == color and self.board[x+1][y] == color and self.board[x+2][y] == color and self.board[x+3][y] == color:
                    return True
        # vertical
        for x in range(self.width):
            for y in range(self.height - 3):
                if self.board[x][y] == color and self.board[x][y+1] == color and self.board[x][y+2] == color and self.board[x][y+3] == color:
                    return True
        # / diagonal
        for x in range(self.width - 3):
            for y in range(3, self.height):
                if self.board[x][y] == color and self.board[x+1][y-1] == color and self.board[x+2][y-2] == color and self.board[x+3][y-3] == color:
                    return True
        # \ diagonal
        for x in range(self.width - 3):
            for y in range(self.height - 3):
                if self.board[x][y] == color and self.board[x+1][y+1] == color and self.board[x+2][y+2] == color and self.board[x+3][y+3] == color:
                    return True
        return False

    def printBoard(self):
        self.interface.printBoard(self)
