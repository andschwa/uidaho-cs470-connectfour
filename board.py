import copy
import error


class Board:
    def __init__(self, interface, width=7, height=6):
        self.board = []
        self.width = width
        self.height = height
        self.interface = interface
        for _ in range(self.width):
            self.board.append([None] * self.height)

    def get_board(self):
        return copy.deepcopy(self.board)

    def valid_move(self, column, board=None):
        if board is None:
            board = self.get_board()
        if column < self.width:
            row = self._next_lowest(column, board)
            if row is None:
                return None
            if board[column][row] is None:
                return row
        else:
            return None

    def make_move(self, column, color):
        row = self.valid_move(column)
        if row is None:
            raise error.InvalidMoveError
        self.board[column][row] = color
        return (column, row)

    def _next_lowest(self, column, board):
        for row, value in enumerate(board[column]):
            if value is None:
                return row
        return None

    def player_won(self, color):
        # horizontal
        for x in range(self.width - 3):
            for y in range(self.height):
                if (self.board[x][y] == color and
                    self.board[x+1][y] == color and
                    self.board[x+2][y] == color and
                    self.board[x+3][y] == color):
                    return True
        # vertical
        for x in range(self.width):
            for y in range(self.height - 3):
                if (self.board[x][y] == color and
                    self.board[x][y+1] == color and
                    self.board[x][y+2] == color and
                    self.board[x][y+3] == color):
                    return True
        # / diagonal
        for x in range(self.width - 3):
            for y in range(3, self.height):
                if (self.board[x][y] == color and
                    self.board[x+1][y-1] == color and
                    self.board[x+2][y-2] == color and
                    self.board[x+3][y-3] == color):
                    return True
        # \ diagonal
        for x in range(self.width - 3):
            for y in range(self.height - 3):
                if (self.board[x][y] == color and
                    self.board[x+1][y+1] == color and
                    self.board[x+2][y+2] == color and
                    self.board[x+3][y+3] == color):
                    return True
        return False

    def is_full(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.board[x][y] is None:
                    return False
        return True

    def print_board(self):
        self.interface.print_board(self)
