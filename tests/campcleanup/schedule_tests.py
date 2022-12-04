import unittest
from campcleanup.schedule import read_cleanup_schedule


class ScheduleTests(unittest.TestCase):
    def test_read_schedule(self):
        schedule = read_cleanup_schedule('cleanup_schedule.txt')

        self.assertEqual(len(schedule.pairs), 6)
        self.assertListEqual(schedule.pairs[2].first.sections, [5, 6, 7])
        self.assertListEqual(schedule.pairs[3].second.sections, [3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
