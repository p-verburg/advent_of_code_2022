class Rucksack:
    def __init__(self, content=[]):
        content = content.strip()
        item_count = len(content)
        half = int(item_count / 2)
        self.left_compartment = content[0:half]
        self.right_compartment = content[half:]

    def find_common_items(self):
        return set(self.left_compartment).intersection(self.right_compartment)

    def all_items(self):
        return self.left_compartment + self.right_compartment


def find_double_packed_items(rucksacks):
    double_items = []
    for rucksack in rucksacks:
        double_items.extend(rucksack.find_common_items())

    return double_items


def read_packing_list(path):
    rucksacks = []

    with open(path) as file:
        for line in file:
            if line and line.strip():
                rucksacks.append(Rucksack(line))

    return rucksacks


def find_common_items(rucksacks):
    if not rucksacks:
        return []

    if len(rucksacks) == 1:
        return rucksacks[0].all_items()

    common_items = set(rucksacks[0].all_items())

    for i in range(1, len(rucksacks)):
        common_items = common_items.intersection(rucksacks[i].all_items())

    return list(common_items)


def find_security_badges(rucksacks, group_size):
    if group_size < 1:
        raise ValueError('Group size should be greater than 0')

    badges = []

    for i in range(0, len(rucksacks), group_size):
        group_badges = find_common_items(rucksacks[i:i + group_size])

        if len(group_badges) != 1:
            raise ValueError('Exactly one badge was not found for group ' + str(int(i/3)))

        badges.extend(group_badges)

    return badges
