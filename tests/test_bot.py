import unittest
from classes import Bot, Player, Board, Token


def make_field(field, bot, player):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 'x':
                field[i][j] = Token.Token(bot, 'x')
            elif field[i][j] == 'o':
                field[i][j] = Token.Token(player, 'o')
    return field


class TestBot(unittest.TestCase):

    def setUp(self):
        self.bot = Bot.Bot('Bot', 'x')
        self.player = Player.Player('Player', 'o')
        self.board = Board.Board()

    def test_bot_init(self):
        self.assertEqual(self.bot.get_name(), 'Bot')
        self.assertEqual(self.bot.get_type(), 'x')
        self.assertTrue(self.bot.is_AI)

    def test_make_best_move(self):
        # Assume an initial state where the bot can win in the next move
        self.board.set_field(make_field([['x', 'o', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], self.bot, self.player))
        best_move = self.bot.make_best_move(self.board, self.player)
        self.assertEqual(best_move[0], 1)

    def test_minimax(self):
        # Assume an initial state where the bot can win in the next move
        self.board.set_field(make_field([['x', 'o', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], self.bot, self.player))
        score, move = self.bot.minimax(self.board, True, self.player)
        self.assertEqual(score, 1)

    def test_is_win(self):
        # Assume an initial state where the bot is winning
        self.board.set_field(make_field([['x', 'x', 'x'], ['o', ' ', ' '], ['o', ' ', ' ']], self.bot, self.player))
        self.assertEqual(self.bot.is_win(self.board, self.player), (0, 1))

        # Assume a state where the player is winning
        self.board.set_field(make_field([['o', 'o', 'o'], ['x', ' ', ' '], ['x', ' ', ' ']], self.bot, self.player))
        self.assertEqual(self.bot.is_win(self.board, self.player), (1, 0))

        # Assume a state where the game is a tie
        self.board.set_field(make_field([['o', 'x', 'o'], ['x', 'x', 'o'], ['o', 'o', 'x']], self.bot, self.player))
        self.assertEqual(self.bot.is_win(self.board, self.player), (1, 1))

if __name__ == '__main__':
    unittest.main()
