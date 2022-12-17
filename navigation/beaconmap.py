import re

from geometry.grid import ExtendableGrid, ValueEncoder, print_grid
from geometry.point import Point2D

UNKNOWN = -1
EMPTY = 0
BEACON = 1
SENSOR = 2
OUTSIDE = 999


class BeaconMap(ExtendableGrid):
    def __init__(self):
        super().__init__(UNKNOWN, OUTSIDE)

    def add_sensor(self, sensor, beacon):
        distance = calculate_sensor_range(sensor, beacon)
        self.extend_vertical(sensor.y - distance - 1, sensor.y + distance + 1)
        self.extend_horizontal(sensor.x - distance - 1, sensor.x + distance + 1)
        self.set_value(beacon.x, beacon.y, BEACON)
        self.set_value(sensor.x, sensor.y, SENSOR)
        for distance_y in range(-distance, distance + 1):
            y = sensor.y + distance_y
            for distance_x in range(-distance + abs(distance_y), distance - abs(distance_y) + 1):
                x = sensor.x + distance_x
                if self.get_value(x, y) == UNKNOWN:
                    self.set_value(x, y, EMPTY)


def read_sensors(file):
    sensor_list = []
    regex = re.compile(r'Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)')
    for line in file:
        match = regex.search(line)
        sensor = Point2D(int(match.group(1)), int(match.group(2)))
        beacon = Point2D(int(match.group(3)), int(match.group(4)))
        # print(f'{sensor} -> {beacon}')
        sensor_list.append((sensor, beacon))
    return sensor_list


def calculate_sensor_range(sensor, beacon):
    difference = sensor - beacon
    sensor_range = abs(difference.x) + abs(difference.y)
    return sensor_range


def construct_map_row(sensor_list, y):
    row = []
    start_x = 0
    end_x = 0
    for (sensor, beacon) in sensor_list:
        sensor_range = calculate_sensor_range(sensor, beacon)
        distance = abs(sensor.y - y)
        sensor_range -= distance
        if sensor_range >= 0:
            if len(row) == 0:
                row = [UNKNOWN] * (1 + 2*sensor_range)
                start_x = sensor.x - sensor_range
                end_x = sensor.x + sensor_range
            else:
                shift = start_x - (sensor.x - sensor_range)
                if shift > 0:
                    row = [UNKNOWN] * shift + row
                    start_x -= shift
                grow = sensor.x + sensor_range - end_x
                if grow > 0:
                    row.extend([UNKNOWN] * grow)
                    end_x += grow

            if sensor.y == y:
                index = sensor.x - start_x
                row[index] = SENSOR
            if beacon.y == y:
                index = beacon.x - start_x
                row[index] = BEACON

            for x in range(sensor.x - sensor_range, sensor.x + sensor_range + 1):
                index = x - start_x
                if row[index] == UNKNOWN:
                    row[index] = EMPTY

    return start_x, row


def count_empty_in_row(row):
    count = 0
    for value in row:
        if value == EMPTY:
            count += 1
    return count


def calculate_sensor_ranges(sensor_list):
    sensor_range_list = []
    for (sensor, beacon) in sensor_list:
        sensor_range = calculate_sensor_range(sensor, beacon)
        sensor_range_list.append((sensor, beacon, sensor_range))
    return sensor_range_list


def read_beacon_map(file):
    beacon_map = BeaconMap()
    sensor_list = read_sensors(file)
    for (sensor, beacon) in sensor_list:
        beacon_map.add_sensor(sensor, beacon)
    return beacon_map


class BeaconMapEncoder(ValueEncoder):
    def __init__(self):
        super().__init__({
            UNKNOWN: '.',
            EMPTY: '#',
            BEACON: 'B',
            SENSOR: 'S'
        }, '.')


def print_beacon_map(beacon_map: BeaconMap):
    return print_grid(beacon_map, BeaconMapEncoder())
