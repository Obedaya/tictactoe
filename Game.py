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
        option = self._view.print_menu()
        if option == 1:
            self._player1 = p.Player(self._view.get_input_playername(1), 'x')
            self._player2 = p.Player(self._view.get_input_playername(2), 'o')
        elif option == 2:
            #load game
            None
        elif option == 3:
            quit()


    def is_valid_move(self, move):
        x, y = move
        field = self._board.get_field()
        if field[x][y] == " ":
            return True
        else:
            return False

    def is_win(self):
        field = self._board.get_field()
        # Check for diagonal win
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
                    return False
        # No winner yet
        return None

    def round(self, player):
        self._view.print_next_player(player)
        field = self._board.get_field()
        self._view.print_field(field)
        move = self._view.get_input_move()
        if self.is_valid_move(move):
            token = t.Token(player, player.get_type())
            self._board.make_move(move, token)
        else:
            self._view.print_nvm()
            self.round(player)

    def end_game(self, option):
        if option == "tie":
            self._view.print_tie()
        else:
            self._view.print_winner(option.get_name())

    def main(self):
        game_running = True
        self.start_game()
        current_player = self._view.get_first_player(self._player1, self._player2)
        self._view.print_tutorial()

        while game_running:
            self.round(current_player)

            if self._round_number >= 4:
                condition = self.is_win()
                if condition == "tie" or condition is not False:
                    field = self._board.get_field()
                    self._view.print_field(field)
                    self.end_game(condition)
                    game_running = False

            self._round_number += 1
            if current_player == self._player1:
                current_player = self._player2
            else:
                current_player = self._player1

        self._view.end()
