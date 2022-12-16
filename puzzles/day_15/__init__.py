from navigation.beaconmap import read_sensors, construct_map_row, count_empty_in_row, find_signal

with open('beacon_map.txt') as file:
    sensor_list = read_sensors(file)

_, row = construct_map_row(sensor_list, 2000000)

count = count_empty_in_row(row)

print(count)

locations = find_signal(sensor_list, 0, 4000000)
assert(len(locations) == 1)
location = locations[0]
print(4000000*location.x + location.y)
