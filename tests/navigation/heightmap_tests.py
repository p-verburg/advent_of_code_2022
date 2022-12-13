import unittest
from navigation.heightmap import read_map, HeightMap, find_shortest_path, IsPoint, \
    HasHeight


class HeightMapTests(unittest.TestCase):
    def test_read_map(self):
        height_map = read_map('test_map.txt')

        self.assertEqual(8, height_map.width)
        self.assertEqual(5, height_map.height)

        self.assertEqual([0, 0], height_map.start)
        self.assertEqual([5, 2], height_map.end)

    def test_find_shortest_path(self):
        height_map = HeightMap([
            "Sabqponm",
            "abcryxxl",
            "accszExk",
            "acctuvwj",
            "abdefghi"
        ])

        destination = IsPoint(height_map.start)
        shortest_path = find_shortest_path(height_map, destination)

        self.assertEqual(31, len(shortest_path) - 1)

    def test_find_shortest_path_from_level(self):
        height_map = HeightMap([
            "Sabqponm",
            "abcryxxl",
            "accszExk",
            "acctuvwj",
            "abdefghi"
        ])

        destination = HasHeight(0)
        shortest_path = find_shortest_path(height_map, destination)

        self.assertEqual(29, len(shortest_path) - 1)


if __name__ == '__main__':
    unittest.main()
