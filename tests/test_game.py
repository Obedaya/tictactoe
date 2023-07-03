import unittest
from unittest import mock
from classes import Board as b
from classes import Player as p
from classes import View as v
from classes import Token as t
from classes import FileHandler as fh
from classes import Bot
from classes import Game
from unittest.mock import patch


class MockView:
    # This mock class is used to simulate user input.
    def print_menu(self):
        return 1

    def get_input_playername(self, player_number):
        return f'Player{player_number}'

    def get_first_player(self, player1, player2):
        return player1

    def print_next_player(self, player):
        pass

    def print_field(self, field):
        pass

    def get_input_move(self):
        return (0, 0)

    def print_nvm(self):
        pass

    def print_tutorial(self):
        pass

    def end(self):
        pass

    def print_winner(self, player_name):
        pass

    def print_tie(self):
        pass

    def print_list_savegames(self, savegames):
        pass


class MockViewAI(MockView):
    # This class extends the MockView class to simulate AI behavior.
    def get_input_move(self):
        return None  # AI does not provide move input

    def get_input_playername(self, player_number):
        return 'AI' if player_number == 2 else super().get_input_playername(player_number)


class MockGameState:
    # This mock class is used to simulate a saved game state.
    def __init__(self, player1_name='Player1', player2_name='Player2', field_state=None, round_number=1):
        self._player1 = p.Player(player1_name, 'x')
        self._player2 = p.Player(player2_name, 'o')
        self._board = b.Board()
        if field_state:
            self._board.set_field(field_state)
        self._round_number = round_number
        self._current_player = self._player1

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game.Game()
        self.game._view = MockView()

    def test_start_game(self):
        self.game.start_game()

        # Assert that players were set up correctly
        self.assertEqual(self.game._player1.get_name(), 'Player1')
        self.assertEqual(self.game._player2.get_name(), 'Player2')
        self.assertEqual(self.game._current_player.get_name(), 'Player1')

    def test_round(self):
        self.game.start_game()
        self.game.round(self.game._current_player)

        # Assert that a move was made on the board
        self.assertEqual(self.game._board.get_field()[0][0].token_type, 'x')

    def test_is_valid_move(self):
        self.game.start_game()

        self.assertTrue(self.game._board.is_valid_move((0, 0)))
        self.game._board.make_move((0, 0), t.Token(self.game._current_player, self.game._current_player.get_type()))
        self.assertFalse(self.game._board.is_valid_move((0, 0)))

    def test_is_win(self):
        self.game.start_game()

        self.assertFalse(self.game.is_win())

        for i in range(3):
            self.game._board.make_move((i, 0), t.Token(self.game._current_player, self.game._current_player.get_type()))

        self.assertEqual(self.game.is_win(), self.game._current_player)

    def test_start_game_option2(self):
        self.game._view.print_menu = lambda: 2
        self.game._view.get_input_file_path = lambda: 'test'
        self.game._file_handler.load_game_state = lambda x: MockGameState()

        self.game.start_game()

        # Assert that the game state was loaded correctly
        self.assertEqual(self.game._player1.get_name(), 'Player1')
        self.assertEqual(self.game._player2.get_name(), 'Player2')
        self.assertEqual(self.game._board.get_field(), MockGameState()._board.get_field())
        self.assertEqual(self.game._round_number, MockGameState()._round_number)

    def test_start_game_option3(self):
        self.game._view.print_menu = lambda: 3

        self.game.start_game()

        # Assert that AI player was set up correctly
        self.assertEqual(self.game._player2.get_name(), 'AI')

    def test_start_game_option4(self):
        self.game._view.print_menu = lambda: 4

        with self.assertRaises(SystemExit):
            self.game.start_game()

    def test_pause_game(self):
        self.game._view.get_input_file_path = lambda: 'test'
        self.game._file_handler.save_game_state = mock.Mock()

        with self.assertRaises(SystemExit):
            self.game.pause_game()

        # Assert that the game state was saved correctly
        self.game._file_handler.save_game_state.assert_called_with('test', self.game)

    def test_end_game(self):
        self.game.start_game()
        self.game._view.print_winner = mock.Mock()
        self.game._view.print_tie = mock.Mock()

        self.game.end_game(self.game._player1)
        self.game._view.print_winner.assert_called_once_with(self.game._player1.get_name())

        self.game._view.print_tie.assert_not_called()

        self.game._view.print_winner.reset_mock()
        self.game._view.print_tie.reset_mock()

        self.game.end_game('tie')

        self.game._view.print_winner.assert_not_called()
        self.game._view.print_tie.assert_called_once()


if __name__ == '__main__':
    unittest.main()