def read_tree_map(path):
    tree_map = []

    with open(path) as file:
        for line in file:
            tree_map.append([])
            row = tree_map[-1]
            for digit in line.strip():
                tree_map[-1].append(int(digit))

    return tree_map
