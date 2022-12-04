from packing.items import get_total_item_priority
from packing.rucksacks import read_packing_list, find_double_packed_items, find_security_badges

rucksacks = read_packing_list('packing_list.txt')

double_items = find_double_packed_items(rucksacks)

total_priority = get_total_item_priority(double_items)

print(total_priority)

badges = find_security_badges(rucksacks, 3)

total_priority = get_total_item_priority(badges)

print(total_priority)
