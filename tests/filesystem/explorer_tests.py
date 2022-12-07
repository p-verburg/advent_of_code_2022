import unittest

from filesystem.explorer import Explorer
from filesystem.tree import sum_directory_sizes
from tree_tests import create_directory_structure


class ExplorerTests(unittest.TestCase):
    def test_find_small_directories(self):
        root = create_directory_structure()
        explorer = Explorer(root)

        small_directories = explorer.find_directories_smaller_than(100000)

        self.assertEqual(2, len(small_directories))

        total_size = sum_directory_sizes(small_directories)

        self.assertEqual(95437, total_size)


if __name__ == '__main__':
    unittest.main()
