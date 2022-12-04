import unittest
from campcleanup.schedule import read_cleanup_schedule, Cleaner, CleanerPair


class ScheduleTests(unittest.TestCase):
    def test_read_schedule(self):
        schedule = read_cleanup_schedule('cleanup_schedule.txt')

        self.assertEqual(len(schedule.pairs), 6)
        self.assertListEqual(schedule.pairs[2].first.sections, [5, 6, 7])
        self.assertListEqual(schedule.pairs[3].second.sections, [3, 4, 5, 6, 7])


class CleanerPairTests(unittest.TestCase):
    def test_partially_overlapping(self):
        first = Cleaner([2, 3, 4])
        second = Cleaner([3, 4, 5])
        pair = CleanerPair(first, second)

        are_overlapping = pair.are_fully_overlapping()

        self.assertEqual(are_overlapping, False)

    def test_first_contains_second(self):
        first = Cleaner([2, 3, 4])
        second = Cleaner([3, 4])
        pair = CleanerPair(first, second)

        are_overlapping = pair.are_fully_overlapping()

        self.assertEqual(are_overlapping, True)

    def test_second_contains_first(self):
        first = Cleaner([2, 3, 4])
        second = Cleaner([1, 2, 3, 4, 5, 6])
        pair = CleanerPair(first, second)

        are_overlapping = pair.are_fully_overlapping()

        self.assertEqual(are_overlapping, True)


if __name__ == '__main__':
    unittest.main()
