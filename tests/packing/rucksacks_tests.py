import unittest

from packing.items import get_total_item_priority
from packing.rucksacks import Rucksack, read_packing_list, find_double_packed_items, find_common_items, \
    find_security_badges


class PackingListReaderTests(unittest.TestCase):
    def test_read_empty_file(self):
        rucksacks = read_packing_list('empty_file.txt')

        self.assertEqual(len(rucksacks), 0)

    def test_read_file_with_empty_lines(self):
        rucksacks = read_packing_list('file_with_empty_lines.txt')

        self.assertEqual(len(rucksacks), 0)

    def test_read_packing_list(self):
        rucksacks = read_packing_list('test_file.txt')

        self.assertEqual(len(rucksacks), 6)
        self.assertEqual(rucksacks[3].left_compartment, "wMqvLMZHhHMvwLH")
        self.assertEqual(rucksacks[3].right_compartment, "jbvcjnnSBnvTQFn")


class PackingErrorsTests(unittest.TestCase):
    def test_find_double_packed_items(self):
        rucksacks = read_packing_list('test_file.txt')

        items = find_double_packed_items(rucksacks)

        self.assertIsNotNone(items)
        self.assertListEqual(items, ['p', 'L', 'P', 'v', 't', 's'])

    def test_find_total_priority_of_double_packed_items(self):
        rucksacks = read_packing_list('test_file.txt')
        items = find_double_packed_items(rucksacks)

        total_priority = get_total_item_priority(items)

        self.assertEqual(total_priority, 157)


class SecurityBadgesTests(unittest.TestCase):
    def test_find_common_items_no_rucksacks(self):
        common_items = find_common_items([])

        self.assertEqual(len(common_items), 0)

    def test_find_common_items_single_rucksack(self):
        rucksack = Rucksack('feiGHopzJT')

        common_items = find_common_items([rucksack])

        self.assertEqual(common_items, rucksack.all_items())

    def test_find_common_items_from_two(self):
        rucksacks = [Rucksack('feiGHopzJT'), Rucksack('asPQJbXYwq')]

        common_items = find_common_items(rucksacks)

        self.assertEqual(common_items, ['J'])

    def test_find_common_items(self):
        rucksacks = read_packing_list('test_file.txt')

        badges = find_security_badges(rucksacks, 3)

        self.assertListEqual(badges, ['r', 'Z'])


if __name__ == '__main__':
    unittest.main()
