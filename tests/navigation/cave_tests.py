import unittest

from navigation.cave import build_map, EMPTY, ROCK, print_map


class CaveMapTests(unittest.TestCase):
    def test_build_map(self):
        with open('test_cave_map.txt') as file:
            cave_map = build_map(file)

        # print_map(cave_map)

        self.assertEqual(494, cave_map.left)
        self.assertEqual(503, cave_map.right)
        self.assertEqual(10, cave_map.width)
        self.assertEqual(10, len(cave_map.rows))

        self.assertEqual(EMPTY, cave_map.get_terrain(499, 5))

        self.assertEqual(ROCK, cave_map.get_terrain(498, 4))
        self.assertEqual(ROCK, cave_map.get_terrain(498, 5))
        self.assertEqual(ROCK, cave_map.get_terrain(498, 6))
        self.assertEqual(ROCK, cave_map.get_terrain(497, 6))
        self.assertEqual(ROCK, cave_map.get_terrain(496, 6))

        self.assertEqual(ROCK, cave_map.get_terrain(503, 4))
        self.assertEqual(ROCK, cave_map.get_terrain(502, 7))
        self.assertEqual(ROCK, cave_map.get_terrain(494, 9))


    def test_drop_sand(self):
        with open('test_cave_map.txt') as file:
            cave_map = build_map(file)

        grains_resting = cave_map.drop_sand()

        print_map(cave_map)

        self.assertEqual(24, grains_resting)


if __name__ == '__main__':
    unittest.main()
