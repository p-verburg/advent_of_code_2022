from navigation.beaconmap import read_sensors, construct_map_row, count_empty_in_row

with open('beacon_map.txt') as file:
    sensor_list = read_sensors(file)

row = construct_map_row(sensor_list, 2000000)

count = count_empty_in_row(row)

print(count)
