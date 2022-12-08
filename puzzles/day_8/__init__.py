from forest.treecoverage import TreeMap
from forest.treemapreader import read_tree_map

tree_height_map = read_tree_map('tree_map.txt')

tree_map = TreeMap(tree_height_map)

visible_tree_count = tree_map.count_visible()

print(visible_tree_count)
