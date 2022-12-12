from navigation.heightmap import read_map, find_shortest_path

height_map = read_map('height_map.txt')

shortest_path = find_shortest_path(height_map)

print(len(shortest_path) - 1)
