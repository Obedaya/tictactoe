import os
import unittest
from unittest import mock
from classes import FileHandler as fh
from classes import Game

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_handler = fh.FileHandler()
        self.game = Game.Game()
        self.test_file_path = 'test'  # your test game state file

    def test_save_game_state(self):
        # Mocking the open function to prevent actual file write
        with mock.patch('builtins.open', mock.mock_open()) as mocked_open:
            self.file_handler.save_game_state(self.test_file_path, self.game)
            # Check if file open has been called with the correct arguments
            mocked_open.assert_called_once_with('data/savegames/' + self.test_file_path, 'wb')

    def test_load_game_state(self):
        loaded_game_state = self.file_handler.load_game_state(self.test_file_path)
        self.assertIsInstance(loaded_game_state, Game.Game)

    def test_get_list_savegames(self):
        savegames_list = self.file_handler.get_list_savegames()
        self.assertIn(self.test_file_path, savegames_list)


if __name__ == '__main__':
    unittest.main()
