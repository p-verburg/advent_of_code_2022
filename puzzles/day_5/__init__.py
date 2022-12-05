from copy import deepcopy
from packing.crates import read_cargo_file, move_9000, move_9001, get_top_crates

stacks, moves = read_cargo_file('cargo_stacks.txt')

for move in moves:
    move_9000(stacks, move)

top_crates = get_top_crates(stacks)

print(top_crates)

stacks, moves = read_cargo_file('cargo_stacks.txt')

for move in moves:
    move_9001(stacks, move)

top_crates = get_top_crates(stacks)

print(top_crates)
