from classes import Board as b
from classes import Player as p
from classes import View as v
from classes import Token as t
from classes import FileHandler as fh
from classes import Bot


class Game:
    _file_handler = None
    _board = None
    _view = None
    _player1 = None
    _player2 = None
    _current_player = None
    _round_number = 0

    def __init__(self):
        self._board = b.Board()
        self._view = v.View()
        self._file_handler = fh.FileHandler()

    def start_game(self):
        option = self._view.print_menu()
        if option == 1:
            self._player1 = p.Player(self._view.get_input_playername(1), 'x')
            self._player2 = p.Player(self._view.get_input_playername(2), 'o')
            if self._player1 == 'q' or self._player2 == 'q':
                quit()
            self._current_player = self._view.get_first_player(self._player1, self._player2)
        elif option == 2:
            self._view.print_list_savegames(self._file_handler.get_list_savegames())
            file_path = self._view.get_input_file_path()
            game_state = self._file_handler.load_game_state(file_path)

            self._player1 = game_state._player1
            self._player2 = game_state._player2
            self._board = game_state._board
            self._round_number = game_state._round_number
            self._current_player = game_state._current_player

        elif option == 3:
            self._player2 = Bot.Bot("AI", 'o')
            #self._player1 = Bot.Bot("AI2", 'x')
            self._player1 = p.Player(self._view.get_input_playername(1), 'x')
            if self._player1 == 'q':
                quit()
            self._current_player = self._player1

        elif option == 4:
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
                    # No winner or tie yet
                    return False
        # The game is a tie
        return "tie"

    def round(self, player):
        self._view.print_next_player(player)
        field = self._board.get_field()
        self._view.print_field(field)

        if not player.is_AI:
            move = self._view.get_input_move()
            if move == 'q':
                self.pause_game()
            if self.is_valid_move(move):
                token = t.Token(player, player.get_type())
                self._board.make_move(move, token)
            else:
                self._view.print_nvm()
                self.round(player)
        else:
            if player == self._player1:
                inactive_player = self._player2
            else:
                inactive_player = self._player1
            move = player.make_best_move(self._board, inactive_player)
            self._view.print_move(move[1])

    def end_game(self, option):
        if option == "tie":
            self._view.print_tie()
        else:
            self._view.print_winner(option.get_name())

    def pause_game(self):
        file_path = self._view.get_input_file_path()
        self._file_handler.save_game_state(file_path, self)
        quit()

    def main(self):
        game_running = True
        self.start_game()
        if self._current_player == 'q':
            quit()
        self._view.print_tutorial()

        while game_running:
            self.round(self._current_player)

            if self._round_number >= 4:
                condition = self.is_win()
                if condition == "tie" or condition is not False:
                    field = self._board.get_field()
                    self._view.print_field(field)
                    self.end_game(condition)
                    game_running = False

            self._round_number += 1
            if self._current_player == self._player1:
                self._current_player = self._player2
            else:
                self._current_player = self._player1

        self._view.end()
