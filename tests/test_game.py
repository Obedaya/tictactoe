import unittest
from classes import Board as b
from classes import Player as p
from classes import View as v
from classes import Token as t
from classes import FileHandler as fh
from classes import Bot
from classes import Game

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

if __name__ == '__main__':
    unittest.main()
