from functools import cmp_to_key

from communication.packetorder import read_all_packets, are_in_right_order, compare, append_divider_packets, \
    find_divider_packets

with open('distress_signal.txt') as file:
    pairs = read_all_packets(file)

sum_ordered_pairs = 0

for i in range(0, len(pairs)):
    result = are_in_right_order(pairs[i].left, pairs[i].right)

    if not not result:
        sum_ordered_pairs += i + 1

print(sum_ordered_pairs)

packets = []
for pair in pairs:
    packets.append(pair.left)
    packets.append(pair.right)
append_divider_packets(packets)

sorted_packets = sorted(packets, key=cmp_to_key(compare))
indices = find_divider_packets(sorted_packets)

print(indices[0] * indices[1])
