import math
import copy
from classes import Player as p
from classes import Token as t


class Bot(p.Player):
    def __init__(self):
        super().__init__("AI", 'o')
        self.is_AI = True

    def make_best_move(self, board):
        board_copy = copy.deepcopy(board)
        bestScore = -math.inf
        bestMove = None
        for move in self.get_possible_moves(board_copy):
            board_copy.make_move(move, t.Token(self, self.get_type()))
            score = self.minimax(False, self, board_copy)
            board_copy.undo()
            if score > bestScore:
                bestScore = score
                bestMove = move
        board.make_move(bestMove, t.Token(self, self.get_type()))

    def get_possible_moves(self, board):
        field = board.get_field()
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if field[i][j] == " ":
                    possible_moves.append((i, j))
        return possible_moves

    def get_state(self, board):
        field = board.get_field()
        if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
            if not isinstance(field[1][1], str):
                return field[1][1].player
        # Check for vertical or horizontal win
        for i in range(3):
            if field[i][0] == field[i][1] == field[i][2] or field[0][i] == field[1][i] == field[2][i]:
                if not isinstance(field[i][i], str):
                    return field[i][i].player
        # Check for tie
        for i in range(3):
            for j in range(3):
                if field[i][j] == " ":
                    # No winner or tie yet
                    return -1
        # The game is a tie
        return 0

    def minimax(self, isMaxTurn, maximizerMark, board):
        state = self.get_state(board)
        # If game is a tie
        if state == 0:
            return 0
        elif state != -1:
            return 1 if state.get_name() == "AI" else -1

        scores = []
        for move in self.get_possible_moves(board):
            board.make_move(move, t.Token(self, self.get_type()))
            scores.append(self.minimax(not isMaxTurn, maximizerMark, board))
            board.undo()

        return max(scores) if isMaxTurn else min(scores)
