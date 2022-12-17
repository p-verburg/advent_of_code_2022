from navigation.beaconmap import read_sensors, construct_map_row, count_empty_in_row, find_signal
from navigation.beaconmapcoverage import find_uncharted_zone, find_points_in_polygons

with open('beacon_map.txt') as file:
    sensor_list = read_sensors(file)

_, row = construct_map_row(sensor_list, 2000000)

count = count_empty_in_row(row)

print(count)

uncharted_zone = find_uncharted_zone(sensor_list, (0, 4000000, 0, 4000000))

locations = find_points_in_polygons(uncharted_zone)

assert(len(locations) == 1)
location = locations[0]
print(4000000*location.x + location.y)
