def read_jet_pattern(file):
    pattern = []
    for line in file:
        for char in line:
            if char == '>':
                pattern.append(1)
            elif char == '<':
                pattern.append(-1)
    return pattern
