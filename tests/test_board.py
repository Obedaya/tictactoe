import unittest
from classes import Board as b
from classes import Token as t
from classes import Player as p

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = b.Board()
        self.player = p.Player('TestPlayer', 'x')
        self.token = t.Token(self.player, self.player.get_type())

    def test_init(self):
        # Test that the board is initialized correctly
        self.assertEqual(self.board.get_field(), [[' '] * 3 for _ in range(3)])

    def test_make_move(self):
        # Test that a move is made correctly
        self.board.make_move((0, 0), self.token)
        self.assertEqual(self.board.get_field()[0][0], self.token)

    def test_set_field(self):
        # Test that the board can be set manually
        new_field = [[' '] * 3 for _ in range(3)]
        new_field[1][1] = self.token
        self.board.set_field(new_field)
        self.assertEqual(self.board.get_field(), new_field)

    def test_is_valid_move(self):
        # Test that a move is identified as valid correctly
        self.assertTrue(self.board.is_valid_move((0, 0)))

        # Test that a move is identified as invalid correctly
        self.board.make_move((0, 0), self.token)
        self.assertFalse(self.board.is_valid_move((0, 0)))


if __name__ == '__main__':
    unittest.main()
