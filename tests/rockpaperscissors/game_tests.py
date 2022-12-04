import unittest
from rockpaperscissors.Game import Move, Round, Game


class GameTests(unittest.TestCase):
    def test_win_rock(self):
        game_round = Round(Move.Rock, Move.Scissors)

        self.assertEqual(game_round.score(), 7)

    def test_draw_rock(self):
        game_round = Round(Move.Rock, Move.Rock)

        self.assertEqual(game_round.score(), 4)

    def test_lose_rock(self):
        game_round = Round(Move.Rock, Move.Paper)

        self.assertEqual(game_round.score(), 1)

    def test_win_paper(self):
        game_round = Round(Move.Paper, Move.Rock)

        self.assertEqual(game_round.score(), 8)

    def test_draw_paper(self):
        game_round = Round(Move.Paper, Move.Paper)

        self.assertEqual(game_round.score(), 5)

    def test_lose_paper(self):
        game_round = Round(Move.Paper, Move.Scissors)

        self.assertEqual(game_round.score(), 2)

    def test_win_scissors(self):
        game_round = Round(Move.Scissors, Move.Paper)

        self.assertEqual(game_round.score(), 9)

    def test_draw_scissors(self):
        game_round = Round(Move.Scissors, Move.Scissors)

        self.assertEqual(game_round.score(), 6)

    def test_lose_scissors(self):
        game_round = Round(Move.Scissors, Move.Rock)

        self.assertEqual(game_round.score(), 3)

    def test_complete_game(self):
        game = Game([Round(Move.Paper, Move.Rock),
                     Round(Move.Rock, Move.Paper),
                     Round(Move.Scissors, Move.Scissors)])

        score = game.score()

        self.assertEqual(score, 15)


if __name__ == '__main__':
    unittest.main()
