import unittest
from packing.items import get_item_priority


class ItemsTests(unittest.TestCase):
    def test_item_priority(self):
        self.assertEqual(get_item_priority('a'), 1)
        self.assertEqual(get_item_priority('m'), 13)
        self.assertEqual(get_item_priority('z'), 26)

        self.assertEqual(get_item_priority('A'), 27)
        self.assertEqual(get_item_priority('M'), 39)
        self.assertEqual(get_item_priority('Z'), 52)


if __name__ == '__main__':
    unittest.main()
