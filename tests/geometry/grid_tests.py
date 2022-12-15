import unittest

from geometry.grid import ExtendableGrid

BLANK = 1
OUTSIDE = 2


class ExtendableGridTests(unittest.TestCase):
    def test_empty_grid(self):
        grid = ExtendableGrid(BLANK, OUTSIDE)

        self.assertEqual(0, grid.left)
        self.assertEqual(0, grid.right)
        self.assertEqual(0, grid.width)

        self.assertEqual(0, grid.top)
        self.assertEqual(0, grid.bottom)
        self.assertEqual(0, grid.height)

    def test_negative_vertical_sliver(self):
        grid = ExtendableGrid(BLANK, OUTSIDE)

        grid.extend_vertical(-4, -1)

        self.assertEqual(0, grid.left)
        self.assertEqual(0, grid.right)
        self.assertEqual(0, grid.width)

        self.assertEqual(-4, grid.top)
        self.assertEqual(-1, grid.bottom)
        self.assertEqual(4, grid.height)

        self.assertEqual(OUTSIDE, grid.get_value(-4, 1))

    def test_negative_horizontal_sliver(self):
        grid = ExtendableGrid(BLANK, OUTSIDE)

        grid.extend_horizontal(-4, -2)

        self.assertEqual(-4, grid.left)
        self.assertEqual(-2, grid.right)
        self.assertEqual(3, grid.width)

        self.assertEqual(0, grid.top)
        self.assertEqual(0, grid.bottom)
        self.assertEqual(0, grid.height)

        self.assertEqual(OUTSIDE, grid.get_value(1, -4))

    def test_negative_blank_grid(self):
        grid = ExtendableGrid(BLANK, OUTSIDE)

        grid.extend_horizontal(-4, -2)
        grid.extend_vertical(-5, -3)

        self.assertEqual(OUTSIDE, grid.get_value(-4, -6))

        self.assertEqual(OUTSIDE, grid.get_value(-5, -5))
        self.assertEqual(BLANK, grid.get_value(-4, -5))

        self.assertEqual(BLANK, grid.get_value(-2, -5))
        self.assertEqual(OUTSIDE, grid.get_value(-1, -5))

        self.assertEqual(BLANK, grid.get_value(-3, -3))
        self.assertEqual(OUTSIDE, grid.get_value(-3, -2))

    def test_get_set_value(self):
        grid = ExtendableGrid(BLANK, OUTSIDE)
        grid.extend_horizontal(2, 6)
        grid.extend_vertical(0, 5)

        self.assertEqual(BLANK, grid.get_value(3, 4))

        grid.set_value(3, 4, 6)
        
        self.assertEqual(6, grid.get_value(3, 4))


if __name__ == '__main__':
    unittest.main()
