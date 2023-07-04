import math
import copy
import random
from classes import Player as p
from classes import Token as t


class Bot(p.Player):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.is_AI = True

    def make_best_move(self, board, inactive_player):
        board_copy = copy.deepcopy(board)
        move = self.minimax(board_copy, True, inactive_player)
        board.make_move(move[1], t.Token(self, self.get_type()))
        return move

    def minimax(self, current_board, is_maximizing, inactive_player, alpha=float('-inf'), beta=float('inf')):
        check_win = self.is_win(current_board, inactive_player)
        if check_win == (1, 1):  # Draw
            return 0, None
        if check_win == (1, 0):  # Player wins
            return -1, None
        if check_win == (0, 1):  # AI wins
            return 1, None

        best_score = float('-inf') if is_maximizing else float('inf')
        best_moves = []

        current_field = current_board.get_field()

        for j in range(0, len(current_field)):
            for k in range(0, len(current_field)):
                if current_field[j][k] == " ":
                    current_field[j][k] = t.Token(inactive_player, inactive_player.get_type()) if not is_maximizing \
                        else t.Token(self, self.get_type())
                    current_board.set_field(current_field)
                    score = self.minimax(current_board, not is_maximizing, inactive_player, alpha, beta)[0]
                    current_field[j][k] = " "
                    current_board.set_field(current_field)

                    if is_maximizing:
                        if score > best_score:
                            best_score = score
                            best_moves = [(j, k)]
                        if score > alpha:
                            alpha = score
                    else:
                        if score < best_score:
                            best_score = score
                            best_moves = [(j, k)]
                        if score < beta:
                            beta = score

                    if beta <= alpha:
                        break

        return best_score, random.choice(best_moves)

    def is_win(self, board, inactive_player):
        field = board.get_field()

        # Check for diagonal win
        if (isinstance(field[0][0], t.Token) and isinstance(field[1][1], t.Token) and isinstance(field[2][2],
                                                                                                 t.Token) and
            field[0][0] == field[1][1] == field[2][2]) or \
                (isinstance(field[0][2], t.Token) and isinstance(field[1][1], t.Token) and isinstance(field[2][0],
                                                                                                      t.Token) and
                 field[0][2] == field[1][1] == field[2][0]):

            if field[1][1].player.is_AI and field[1][1].player != inactive_player:
                return 0, 1
            else:
                return 1, 0

        # Check for vertical or horizontal win
        for i in range(3):
            if (isinstance(field[i][0], t.Token) and isinstance(field[i][1], t.Token) and isinstance(field[i][2],
                                                                                                     t.Token) and
                field[i][0] == field[i][1] == field[i][2]) or \
                    (isinstance(field[0][i], t.Token) and isinstance(field[1][i], t.Token) and isinstance(field[2][i],
                                                                                                          t.Token) and
                     field[0][i] == field[1][i] == field[2][i]):

                if field[i][i].player.is_AI and field[i][i].player != inactive_player:
                    return 0, 1
                else:
                    return 1, 0

        # Check for tie
        if any(" " in row for row in field):
            return 0, 0  # No winner or tie yet

        return 1, 1  # The game is a tie


