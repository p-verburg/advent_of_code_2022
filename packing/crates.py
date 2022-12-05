from containers.stack import Stack


class Move:
    def __init__(self, amount, source, target):
        self.amount = amount
        self.source = source
        self.target = target

    def __eq__(self, other):
        return self.amount == other.amount \
               and self.source == other.source \
               and self.target == other.target


def move_9000(stacks, move):
    for i in range(0, move.amount):
        crate = stacks[move.source - 1].pop()
        stacks[move.target - 1].push(crate)


def move_9001(stacks, move):
    moved_stack = Stack()
    for i in range(0, move.amount):
        moved_stack.push(stacks[move.source - 1].pop())
    for _ in range(0, len(moved_stack)):
        stacks[move.target - 1].push(moved_stack.pop())


COLUMN_WIDTH = 4


def read_cargo_stacks(file):

    stacks = []
    for line in file:
        for i in range(0, len(line), COLUMN_WIDTH):
            stack_index = int(i / COLUMN_WIDTH)
            if stack_index >= len(stacks):
                stacks.append(Stack())
            crate = line[i:i+COLUMN_WIDTH].strip(" []")
            if crate:
                if crate.isdigit():
                    return stacks
                stacks[stack_index].prepend(crate[0])
    return stacks


def read_moves(file):
    moves = []
    for line in file:
        words = line.split()
        if len(words) == 6:
            moves.append(Move(int(words[1]), int(words[3]), int(words[5])))
    return moves


def read_cargo_file(path):
    with open(path) as file:
        cargo = read_cargo_stacks(file)
        moves = read_moves(file)

        return cargo, moves


def get_top_crates(stacks):
    top_crates = ""
    for stack in stacks:
        top_crates += stack.peek()
    return top_crates
