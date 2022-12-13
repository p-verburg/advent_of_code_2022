from navigation.heightmap import read_map, find_shortest_path, IsPoint, HasHeight

height_map = read_map('height_map.txt')

destination = IsPoint(height_map.start)
shortest_path = find_shortest_path(height_map, destination)

print(len(shortest_path) - 1)

destination = HasHeight(0)
shortest_path = find_shortest_path(height_map, destination)

print(len(shortest_path) - 1)
