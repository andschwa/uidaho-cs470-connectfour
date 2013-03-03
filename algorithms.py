import random

import error


class Minimax():
    def __init__(self, board, colors):
        self.board = board
        self.colors = colors

    def _other_color(self, color):
        colors = list(self.colors)
        colors.remove(color)
        return colors[0]

    def best_move(self, color, difficulty):
        player = color
        opponent = self._other_color(color)
        depth = difficulty

        legal_moves = {}
        for column in range(self.board.width):
            if self.board.valid_move(column, self.board.get_board()) is not None:
                temp = self.make_fake_move(self.board.get_board(), column, player)
                legal_moves[column] = -self.search(depth-1, temp, opponent)

        best_alpha = -99999999
        best_move = None
        moves = list(legal_moves.items())
        random.shuffle(moves)
        for move, alpha in moves:
            if alpha >= best_alpha:
                best_alpha = alpha
                best_move = move

        return best_move, best_alpha

    def make_fake_move(self, state, column, color):
        row = self.board.valid_move(column, state)
        if row is None:
            raise error.InvalidMoveError
        state[column][row] = color
        return state

    def search(self, depth, state, player):
        opponent = self._other_color(player)
        legal_moves = []
        for column in range(self.board.width):
            if self.board.valid_move(column, state) is not None:
                legal_moves.append(self.make_fake_move(state, column, player))

        if depth == 0 or legal_moves is None or self.game_over(state):
            return self.value(state, player)

        alpha = -99999999
        for move in legal_moves:
            alpha = max(alpha, -self.search(depth-1, move, opponent))
        return alpha

    def check_for_streak(self, state, color, streak):
        streaks = 0
        for col in range(self.board.width):
            for row in range(self.board.height):
                if state[col][row] == color:
                    streaks += self.vertical_streak(col, row, state, streak)
                    streaks += self.horizontal_streak(col, row, state, streak)
                    streaks += self.diagonal_check(col, row, state, streak)
        return streaks

    def game_over(self, state):
        if (self.check_for_streak(state, self.colors[0], 4) >= 1 or
            self.check_for_streak(state, self.colors[1], 4) >= 1):
            return True
        else:
            return False

    def value(self, state, color):
        player = color
        opponent = self._other_color(player)
        my_fours = self.check_for_streak(state, player, 4)
        my_threes = self.check_for_streak(state, player, 3)
        my_twos = self.check_for_streak(state, player, 2)
        opp_fours = self.check_for_streak(state, opponent, 4)
        #opp_threes = self.check_for_streak(state, opponent, 3)
        #opp_twos = self.check_for_streak(state, opponent, 2)
        if opp_fours > 0:
            return -100000
        else:
            return my_fours*100000 + my_threes*100 + my_twos

    def vertical_streak(self, col, row, state, streak):
        consecutiveCount = 0
        for i in range(row, self.board.height):
            if state[col][i] == state[col][row]:
                consecutiveCount += 1
            else:
                break

        if consecutiveCount >= streak:
            return 1
        else:
            return 0

    def horizontal_streak(self, col, row, state, streak):
        consecutiveCount = 0
        for j in range(col, self.board.width):
            if state[j][row] == state[col][row]:
                consecutiveCount += 1
            else:
                break

        if consecutiveCount >= streak:
            return 1
        else:
            return 0

    def diagonal_check(self, col, row, state, streak):
        total = 0
        # check for diagonals with positive slope
        consecutiveCount = 0
        j = col
        for i in range(row, self.board.height):
            if j > 6:
                break
            elif state[j][i] == state[col][row]:
                consecutiveCount += 1
            else:
                break
            j += 1  # increment column when row is incremented
        if consecutiveCount >= streak:
            total += 1

        # check for diagonals with negative slope
        consecutiveCount = 0
        j = col
        for i in range(row, -1, -1):
            if j > 6:
                break
            elif state[j][i] == state[col][row]:
                consecutiveCount += 1
            else:
                break
            j += 1  # increment column when row is incremented

        if consecutiveCount >= streak:
            total += 1

        return total
