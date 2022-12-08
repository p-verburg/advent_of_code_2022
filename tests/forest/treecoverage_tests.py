import unittest

from forest.treecoverage import TreeMap
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
        grid = [[3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0]]

        forest = TreeMap(grid)

        count = forest.count_visible()

        self.assertEqual(21, count)


if __name__ == '__main__':
    unittest.main()
