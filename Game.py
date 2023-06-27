import Board as b
import Player as p
import View as v
import Token as t


class Game:
    _board = None
    _view = None
    _player1 = None
    _player2 = None

    _round_number = 0

    def __init__(self):
        self._board = b.Board()
        self._view = v.View()

    def start_game(self):
        self._view.print_menu()
        self._player1 = p.Player(self._view.get_input_playername(1), 'x')
        self._player2 = p.Player(self._view.get_input_playername(2), 'o')

    def is_valid_move(self, move):
        x, y = move
        field = self._board.get_field()
        if field[x][y] is None:
            return True
        else:
            return False

    def is_win(self):
        field = self._board.get_field()
        # Check for diagonal win
        if field[0][0].player == field[1][1].player == field[2][2].player \
                or field[0][2].player == field[1][1].player == field[2][0].player:
            return field[1][1].player
        # Check for vertical or horizontal win
        for i in range(3):
            if field[i][0].player == field[i][1].player == field[i][2].player \
                    or field[0][i].player == field[1][i].player == field[2][i].player:
                return field[i][i].player
        # Check for tie
        if all(all(row) for row in field):
            return "tie"
        # No winner yet
        return None

    def round(self, player):
        field = self._board.get_field()
        self._view.print_field(field)
        move = self._view.get_input_move()
        if self.is_valid_move(field, move):
            token = t.Token(player, player.get_type())
            field = self._board.make_move(move, token)
            self._view.print_field(field)
        else:
            self._view.print_nvm()
            self.round(player)

    def end_game(self, option):
        if option == "tie":
            self._view.print_tie()
        else:
            self.view.print_winner(option)

    def main(self):
        game_running = True
        self.start_game()
        current_player = self._view.get_first_player(self._player1, self._player2)

        while game_running:
            self.round(current_player)

            if self._round_number == 5:
                condition = self.is_win()
                if condition == "tie" or condition is not False:
                    self.end_game(condition)
                    game_running = False
                else:
                    self._round_number += 1

        self._view.end()
