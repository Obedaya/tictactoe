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

    def test_is_valid_move(self):
        game = Game.Game()
        game._view = MockView()
        game.start_game()

        self.assertTrue(game.is_valid_move((0, 0)))
        game._board.make_move((0, 0), t.Token(game._current_player, game._current_player.get_type()))
        self.assertFalse(game.is_valid_move((0, 0)))

    def test_is_win(self):
        game = Game.Game()
        game._view = MockView()
        game.start_game()

        self.assertFalse(game.is_win())

        for i in range(3):
            game._board.make_move((i, 0), t.Token(game._current_player, game._current_player.get_type()))

        self.assertEqual(game.is_win(), game._current_player)

if __name__ == '__main__':
    unittest.main()
