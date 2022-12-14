from navigation.cave import build_map, print_map

with open('cave_map.txt') as file:
    cave_map = build_map(file)

grains_rested = cave_map.drop_sand()

# print_map(cave_map)

print(grains_rested)
