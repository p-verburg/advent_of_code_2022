import unittest
from filesystem.tree import File, Directory, get_root_directory


class FileTests(unittest.TestCase):
    def test_create_file(self):
        file = File('hello', 1243)

        self.assertEqual('hello', file.name)
        self.assertEqual(1243, file.size)


def create_directory_structure():
    root = get_root_directory()
    a = root.add_subdirectory('a')
    e = a.add_subdirectory('e')
    e.add_file('i', 584)
    a.add_file('f', 29116)
    a.add_file('g', 2557)
    a.add_file('h.lst', 62596)
    root.add_file('b.txt', 14848514)
    root.add_file('c.dat', 8504156)
    d = root.add_subdirectory('d')
    d.add_file('j', 4060174)
    d.add_file('d.log', 8033020)
    d.add_file('d.ext', 5626152)
    d.add_file('k', 7214296)

    return root


class DirectoryTests(unittest.TestCase):
    def test_create_directory(self):
        root = get_root_directory()
        directory = root.add_subdirectory('world')

        self.assertEqual('world', directory.name)
        self.assertEqual(root, directory.parent)
        self.assertEqual(0, len(directory.subdirectories))
        self.assertEqual(0, len(directory.files))
        self.assertEqual(0, directory.total_size())

    def test_create_directory_single_file(self):
        root = get_root_directory()
        directory = root.add_subdirectory('world')
        directory.add_file('a', 123)

        self.assertListEqual([File('a', 123)], directory.files)
        self.assertEqual(123, directory.total_size())

    def test_directory_structure(self):
        root = create_directory_structure()

        self.assertEqual(48381165, root.total_size())


if __name__ == '__main__':
    unittest.main()
