import random
import sys

import error


class Minimax():
    def __init__(self, board, colors):
        self.board = board
        self.colors = colors
        self.max_player = None

    def _other_color(self, color):
        colors = list(self.colors)
        colors.remove(color)
        return colors[0]

    def best_move(self, color, difficulty):
        player = color
        self.max_player = player
        opponent = self._other_color(color)
        depth = difficulty

        legal_moves = {}
        for column in range(self.board.width):
            if (self.board.valid_move(column, self.board.get_board())
                is not None):
                state = self.make_fake_move(self.board.get_board(),
                                            column, player)
                legal_moves[column] = -self.search(state, depth-1, opponent)

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

    def search(self, state, depth, player,
               alpha=-sys.maxsize, beta=sys.maxsize):
        opp = self._other_color(player)
        legal_moves = []
        for column in range(self.board.width):
            if self.board.valid_move(column, state) is not None:
                legal_moves.append(self.make_fake_move(state, column, player))

        if depth == 0 or legal_moves is None or self.game_over(state):
            return self.value(state, player)

        if player == self.max_player:
            for move in legal_moves:
                alpha = max(alpha, -self.search(move, depth-1, opp,
                            alpha, beta))
                if beta <= alpha:
                    break
            return alpha
        else:
            for move in legal_moves:
                beta = min(beta, -self.search(move, depth-1, opp, alpha, beta))
                if beta <= alpha:
                    break
            return beta

    def check_for_streak(self, state, color, streak):
        streaks = 0
        for col in range(self.board.width):
            for row in range(self.board.height):
                if state[col][row] == color:
                    streaks += self.vertical_streak(col, row, state, streak)
                    streaks += self.horizontal_streak(col, row, state, streak)
                    streaks += self.diagonal_streak(col, row, state, streak)
        return streaks

    def game_over(self, state):
        return (self.check_for_streak(state, self.colors[0], 4) >= 1 or
                self.check_for_streak(state, self.colors[1], 4) >= 1)

    def value(self, state, color):
        player = color
        opponent = self._other_color(player)
        my_fours = self.check_for_streak(state, player, 4)
        my_threes = self.check_for_streak(state, player, 3)
        my_twos = self.check_for_streak(state, player, 2)
        opp_fours = self.check_for_streak(state, opponent, 4)
        opp_threes = self.check_for_streak(state, opponent, 3)
        opp_twos = self.check_for_streak(state, opponent, 2)
        if opp_fours > 0:
            return sys.maxsize
        else:
            return (my_fours*10000000 + my_threes*1000 + my_twos*10
                    - opp_threes*10000 - opp_twos*100)

    def vertical_streak(self, icol, irow, state, streak):
        count = 0
        for row in range(irow, self.board.height):
            if state[icol][row] == state[icol][irow]:
                count += 1
            else:
                break
        for row in range(irow, -1, -1):
            if state[icol][row] == state[icol][irow]:
                count += 1
            else:
                break
        return int(count >= streak)

    def horizontal_streak(self, icol, irow, state, streak):
        count = 0
        for col in range(icol, self.board.width):
            if state[col][irow] == state[icol][irow]:
                count += 1
            else:
                break
        for col in range(icol, -1, -1):
            if state[col][irow] == state[icol][irow]:
                count += 1
            else:
                break
        return int(count >= streak)

    def diagonal_streak(self, icol, irow, state, streak):
        total = 0
        # check for diagonals with positive slope
        count = 0
        col = icol
        for row in range(irow, self.board.height):
            if col >= self.board.width or col < 0:
                break
            if state[col][row] == state[icol][irow]:
                count += 1
            else:
                break
            col += 1  # increment column when row is incremented
        total += int(count >= streak)

        # check for diagonals with negative slope
        count = 0
        col = icol
        for row in range(irow, -1, -1):
            if col >= self.board.width or col < 0:
                break
            elif state[col][row] == state[icol][irow]:
                count += 1
            else:
                break
            col += 1  # increment column when row is incremented
        total += int(count >= streak)

        return total
