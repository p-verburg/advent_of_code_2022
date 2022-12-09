import unittest
from rope.ropephysics import RopeTracker


class RopeTrackerTests(unittest.TestCase):
    def test_step_left(self):
        tracker = RopeTracker(2)
        tracker.step_head(-2, 0)

        self.assertEqual((-1, 0), tracker.tail())
        self.assertEqual(tracker.tail(), tracker.trail[-1])

    def test_step_right(self):
        tracker = RopeTracker(2)
        tracker.step_head(2, 0)

        self.assertEqual((1, 0), tracker.tail())
        self.assertEqual(tracker.tail(), tracker.trail[-1])

    def test_step_up(self):
        tracker = RopeTracker(2)
        tracker.step_head(0, 2)

        self.assertEqual((0, 1), tracker.tail())
        self.assertEqual(tracker.tail(), tracker.trail[-1])

    def test_step_down(self):
        tracker = RopeTracker(2)
        tracker.step_head(0, -2)

        self.assertEqual((0, -1), tracker.tail())
        self.assertEqual(tracker.tail(), tracker.trail[-1])

    def test_step_right_up(self):
        tracker = RopeTracker(2)
        tracker.step_head(1, 1)

        self.assertEqual((0, 0), tracker.tail())
        self.assertEqual(tracker.tail(), tracker.trail[-1])

    def test_step_right_up_away(self):
        tracker = RopeTracker(2)
        tracker.step_head(2, 1)

        self.assertEqual((1, 1), tracker.tail())
        self.assertEqual(tracker.tail(), tracker.trail[-1])

    def test_step_bottom_down_away(self):
        tracker = RopeTracker(2)
        tracker.step_head(-1, -2)

        self.assertEqual((-1, -1), tracker.tail())
        self.assertEqual(tracker.tail(), tracker.trail[-1])

    def test_track(self):
        tracker = RopeTracker(2)
        tracker.move_head(4, 0)
        tracker.move_head(0, 4)
        tracker.move_head(-3, 0)
        tracker.move_head(0, -1)
        tracker.move_head(4, 0)
        tracker.move_head(0, -1)
        tracker.move_head(-5, 0)
        tracker.move_head(2, 0)

        positions = tracker.count_distinct_positions()

        self.assertEqual(13, positions)


if __name__ == '__main__':
    unittest.main()
