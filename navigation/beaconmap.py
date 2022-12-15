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
        difference = beacon - sensor
        distance = abs(difference.x) + abs(difference.y)
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

    def count_empty_in_row(self, y):
        y = self.convert_y(y)
        return count_empty_in_row(self.rows[y])


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


def construct_map_row(sensor_list, y):
    row = []
    start_row = 0
    end_row = 0
    for (sensor, beacon) in sensor_list:
        difference = sensor - beacon
        sensor_range = abs(difference.x) + abs(difference.y)
        distance = abs(sensor.y - y)
        sensor_range -= distance
        if sensor_range >= 0:
            if len(row) == 0:
                row = [UNKNOWN] * (1 + 2*sensor_range)
                start_row = sensor.x - sensor_range
                end_row = sensor.x + sensor_range
            else:
                shift = start_row - (sensor.x - sensor_range)
                if shift > 0:
                    row = [UNKNOWN] * shift + row
                    start_row -= shift
                grow = sensor.x + sensor_range - end_row
                if grow > 0:
                    row.extend([UNKNOWN] * grow)
                    end_row += grow

            if sensor.y == y:
                index = sensor.x - start_row
                row[index] = SENSOR
            if beacon.y == y:
                index = beacon.x - start_row
                row[index] = BEACON

            for x in range(sensor.x - sensor_range, sensor.x + sensor_range + 1):
                index = x - start_row
                if row[index] == UNKNOWN:
                    row[index] = EMPTY

    return row


def count_empty_in_row(row):
    count = 0
    for value in row:
        if value == EMPTY:
            count += 1
    return count


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
