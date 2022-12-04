import unittest

from rockpaperscissors.Game import Move
from rockpaperscissors.GameFileReader import read_game_file


class GameFileReaderTests(unittest.TestCase):
    def test_empty_file(self):
        game = read_game_file('empty_file.txt')

        self.assertEqual(len(game.rounds), 0)

    def test_file_with_blank_lines(self):
        game = read_game_file('file_with_blank_lines.txt')

        self.assertEqual(len(game.rounds), 0)

    def test_file(self):
        game = read_game_file('test_file.txt')

        self.assertEqual(len(game.rounds), 3)
        self.assertEqual(game.rounds[0].their_move, Move.Rock)
        self.assertEqual(game.rounds[0].our_move, Move.Rock)
        self.assertEqual(game.rounds[1].their_move, Move.Paper)
        self.assertEqual(game.rounds[1].our_move, Move.Rock)
        self.assertEqual(game.rounds[2].their_move, Move.Scissors)
        self.assertEqual(game.rounds[2].our_move, Move.Rock)


if __name__ == '__main__':
    unittest.main()
