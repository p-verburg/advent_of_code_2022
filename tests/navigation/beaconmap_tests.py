import unittest

from navigation.beaconmap import read_beacon_map, BEACON, SENSOR, print_beacon_map, read_sensors, construct_map_row, \
    count_empty_in_row, find_signal


class BeaconMapTests(unittest.TestCase):
    def test_read_beacon_map(self):
        with open('test_beacon_map.txt') as file:
            beacon_map = read_beacon_map(file)

        print_beacon_map(beacon_map)

        self.assertEqual(BEACON, beacon_map.get_value(15, 3))
        self.assertEqual(SENSOR, beacon_map.get_value(13, 2))

    def test_count_empty_in_map_row(self):
        with open('test_beacon_map.txt') as file:
            beacon_map = read_beacon_map(file)

        count = beacon_map.count_empty_in_row(10)

        self.assertEqual(26, count)

    def test_count_empty_in_single_row(self):
        with open('test_beacon_map.txt') as file:
            sensor_list = read_sensors(file)

        _, row = construct_map_row(sensor_list, 10)

        count = count_empty_in_row(row)

        self.assertEqual(26, count)

    def test_find_signal(self):
        with open('test_beacon_map.txt') as file:
            sensor_list = read_sensors(file)

        locations = find_signal(sensor_list, 0, 20)

        self.assertEqual(1, len(locations))
        self.assertEqual(14, locations[0].x)
        self.assertEqual(11, locations[0].y)


if __name__ == '__main__':
    unittest.main()
