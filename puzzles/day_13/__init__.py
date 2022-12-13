from communication.packetorder import read_all_packets, are_in_right_order

with open('distress_signal.txt') as file:
    pairs = read_all_packets(file)

sum_ordered_pairs = 0

for i in range(0, len(pairs)):
    result = are_in_right_order(pairs[i].left, pairs[i].right)

    if not not result:
        sum_ordered_pairs += i + 1

print(sum_ordered_pairs)
