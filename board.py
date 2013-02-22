class Board:
    def __init__(self):
        self.board = []
        self.width = 7
        self.height = 6
        for x in range(self.width):
            board.append([None] * self.height)

    def makeMove(self, column, color):
        self.board[column][self._nextLowest()] = color

    def _nextLowest(self, column):
        for space in self.board[column]:
            if space is None:
                return space
        raise ColumnFullError

    def moveWon(self, move):
        # horizontal
        for x in range(self.width - 3):
            for y in range(self.height):
                if self.board[x][y] == move and self.board[x+1][y] == move and self.board[x+2][y] == move and self.board[x+3][y] == move:
                    return True
        # vertical
        for x in range(self.width):
            for y in range(self.height - 3):
                if self.board[x][y] == move and self.board[x][y+1] == move and self.board[x][y+2] == move and self.board[x][y+3] == move:
                    return True
        # / diagonal
        for x in range(self.width - 3):
            for y in range(3, self.height):
                if self.board[x][y] == move and self.board[x+1][y-1] == move and self.board[x+2][y-2] == move and self.board[x+3][y-3] == move:
                    return True
        # \ diagonal
        for x in range(self.width - 3):
            for y in range(self.height - 3):
                if self.board[x][y] == move and self.board[x+1][y+1] == move and self.board[x+2][y+2] == move and self.board[x+3][y+3] == move:
                    return True
        return False

