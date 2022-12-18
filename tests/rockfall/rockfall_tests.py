import unittest

from rockfall.jets import read_jet_pattern
from rockfall.bitwise_rocks import Chamber, Dash, print_chamber, Rockfall


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

        # rows are in reverse order, so we start with the bottom
        self.assertEqual(0b11111111, chamber.space[0])
        self.assertEqual(0b10011110, chamber.space[1])

        for row in chamber.space[2:]:
            self.assertEqual(0b10000000, row)

    def test_10_rocks(self):
        with open('test_jet_pattern.txt') as file:
            jet_pattern = read_jet_pattern(file)
        chamber = Chamber(jet_pattern)
        rockfall = Rockfall()

        for _ in range(0, 10):
            chamber.drop_rock(rockfall.get_next_rock())

        print_chamber(chamber)

        self.assertListEqual([
            0b10000000,
            0b10000100,
            0b10000100,
            0b10000110,
            0b11100110,
            0b11111110,
            0b10111000,
            0b10010000,
            0b10111100,
            0b10000110,
            0b10000110,
            0b10000100,
            0b10010100,
            0b10010100,
            0b11111100,
            0b10011100,
            0b10001000,
            0b10011110,
            0b11111111
        ], list(reversed(chamber.space[:19])))

    def test_rock_fall_height(self):
        with open('test_jet_pattern.txt') as file:
            jet_pattern = read_jet_pattern(file)
        chamber = Chamber(jet_pattern)
        rockfall = Rockfall()

        for _ in range(0, 2022):
            chamber.drop_rock(rockfall.get_next_rock())

        self.assertEqual(3068, chamber.get_rock_height())

    def test_lots_of_rockfall_height(self):
        with open('test_jet_pattern.txt') as file:
            jet_pattern = read_jet_pattern(file)
        chamber = Chamber(jet_pattern)
        rockfall = Rockfall()

        for _ in range(0, 1000000000000):
            chamber.drop_rock(rockfall.get_next_rock())

        self.assertEqual(1514285714288, chamber.get_rock_height())


if __name__ == '__main__':
    unittest.main()
