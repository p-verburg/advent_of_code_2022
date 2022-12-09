import unittest
from geometry.point import Point2D


class Point2DTests(unittest.TestCase):
    def test_string(self):
        point = Point2D(34, 56)

        self.assertEqual('(34, 56)', str(point))

    def test_equality(self):
        point = Point2D(2, 5)
        different = Point2D(2, -5)
        same = Point2D(2, 5)

        self.assertEqual(False, point == different)
        self.assertEqual(True, point == same)

    def test_equality_list(self):
        point = Point2D(2, 5)
        different = [2, -5]
        same = [2, 5]

        self.assertEqual(False, point == different)
        self.assertEqual(True, point == same)

    def test_equality_tuple(self):
        point = Point2D(2, 5)
        different = (2, -5)
        same = (2, 5)

        self.assertEqual(False, point == different)
        self.assertEqual(True, point == same)

    def test_addition(self):
        point = Point2D(34, 12)
        other = Point2D(12, -70)

        added = point + other

        self.assertEqual(Point2D(46, -58), added)

    def test_subtraction(self):
        point = Point2D(34, 12)
        other = Point2D(12, -70)

        subtracted = point - other

        self.assertEqual(Point2D(22, 82), subtracted)

    def test_unit(self):
        for x in range(-1, 2):
            for y in range(-1, 2):
                point = Point2D(12 * x, 7 * y)
                unit = point.unit()
                self.assertEqual(Point2D(x, y), unit)


if __name__ == '__main__':
    unittest.main()
