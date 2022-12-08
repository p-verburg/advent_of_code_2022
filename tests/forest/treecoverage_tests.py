import unittest

from forest.treecoverage import TreeMap, ScenicScorer
from forest.treemapreader import read_tree_map


def height_grid():
    return [[3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0]]


class TreeMapReaderTests(unittest.TestCase):
    def test_read_map(self):
        tree_map = read_tree_map('tree_map.txt')

        expected = height_grid()

        self.assertEqual(5, len(tree_map))
        for row in range(0, len(tree_map)):
            self.assertEqual(5, len(tree_map[row]))
            for col in range(0, len(tree_map[row])):
                self.assertEqual(expected[row][col], tree_map[row][col])


class TreeMapTests(unittest.TestCase):
    def test_build_map(self):
        forest = TreeMap(height_grid())

        self.assertEqual(5, len(forest.grid))
        self.assertEqual(5, len(forest.grid[0]))
        self.assertEqual(5, forest.grid[1][2].height)
        self.assertEqual(False, forest.grid[3][4].visible)

    def test_count_visible(self):
        forest = TreeMap(height_grid())

        count = forest.count_visible()

        self.assertEqual(21, count)

    def test_find_highest_scenic_score(self):
        forest = TreeMap(height_grid())

        highest_score = forest.find_highest_scenic_score()

        self.assertEqual(8, highest_score)


def create_scorer():
    forest = TreeMap(height_grid())
    scorer = ScenicScorer(forest)
    return scorer


class ScenicScorerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.scorer = create_scorer()

    def height(self, row, column):
        return self.scorer.grid[row][column].height

    def test_score_left(self):
        score = self.scorer.score_left(1, 2, self.height(1, 2))

        self.assertEqual(1, score)

        score = self.scorer.score_left(3, 2, self.height(3, 2))

        self.assertEqual(2, score)

    def test_score_left_edge(self):
        score = self.scorer.score_left(2, 0, self.height(2, 0))

        self.assertEqual(0, score)

    def test_score_right(self):
        score = self.scorer.score_right(1, 2, self.height(1, 2))

        self.assertEqual(2, score)

        score = self.scorer.score_right(3, 2, self.height(3, 2))

        self.assertEqual(2, score)

    def test_score_right_edge(self):
        score = self.scorer.score_right(2, 4, self.height(2, 4))

        self.assertEqual(0, score)

    def test_score_up(self):
        score = self.scorer.score_up(1, 2, self.height(1, 2))

        self.assertEqual(1, score)

        score = self.scorer.score_up(3, 2, self.height(3, 2))

        self.assertEqual(2, score)

    def test_score_up_edge(self):
        score = self.scorer.score_up(0, 3, self.height(0, 3))

        self.assertEqual(0, score)

    def test_score_down(self):
        score = self.scorer.score_down(1, 2, self.height(1, 2))

        self.assertEqual(2, score)

        score = self.scorer.score_down(3, 2, self.height(3, 2))

        self.assertEqual(1, score)

    def test_score_down_edge(self):
        score = self.scorer.score_down(4, 3, self.height(4, 3))

        self.assertEqual(0, score)

    def test_score(self):
        score = self.scorer.score(1, 2)

        self.assertEqual(4, score)

        score = self.scorer.score(3, 2)

        self.assertEqual(8, score)


if __name__ == '__main__':
    unittest.main()
