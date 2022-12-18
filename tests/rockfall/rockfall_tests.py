import unittest

from rockfall.jets import read_jet_pattern
from rockfall.rocks import Chamber, Dash, EMPTY, ROCK, print_chamber, Rockfall


class JetsTests(unittest.TestCase):
    def test_read_jet_pattern(self):
        pattern = read_jet_pattern([
            "<<>><>>\n",
            "><>>><>>>\n"
        ])

        self.assertListEqual([-1, -1, 1, 1, -1, 1, 1,
                              1, -1, 1, 1, 1, -1, 1, 1, 1],
                             pattern)


class RockfallTests(unittest.TestCase):
    def test_single_rock(self):
        with open('test_jet_pattern.txt') as file:
            jet_pattern = read_jet_pattern(file)
        chamber = Chamber(jet_pattern)

        chamber.drop_rock(Dash())

        # print_chamber(chamber)

        self.assertListEqual([0, 0, 1, 1, 1, 1, 0],
                             chamber.space[0])
        for row in chamber.space[1:]:
            self.assertListEqual([EMPTY] * chamber.width, row)

    def test_10_rocks(self):
        with open('test_jet_pattern.txt') as file:
            jet_pattern = read_jet_pattern(file)
        chamber = Chamber(jet_pattern)
        rockfall = Rockfall()

        for _ in range(0, 10):
            chamber.drop_rock(rockfall.get_next_rock())

        print_chamber(chamber)

        self.assertListEqual([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0],
            [1, 1, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0],
        ], list(reversed(chamber.space[:18])))

    def test_rock_fall_height(self):
        with open('test_jet_pattern.txt') as file:
            jet_pattern = read_jet_pattern(file)
        chamber = Chamber(jet_pattern)
        rockfall = Rockfall()

        for _ in range(0, 2022):
            chamber.drop_rock(rockfall.get_next_rock())

        self.assertEqual(3068, chamber.highest_rock + 1)


if __name__ == '__main__':
    unittest.main()
