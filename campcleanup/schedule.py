class Cleaner:
    def __init__(self, sections=None):
        if sections is None:
            sections = []
        self.sections = sections


class CleanerPair:
    def __init__(self, first_cleaner, second_cleaner):
        self.first = first_cleaner
        self.second = second_cleaner


class CleanupSchedule:
    def __init__(self):
        self.pairs = []

    def add_cleanup_pair(self, pair):
        self.pairs.append(pair)


def parse_assignment(assignment):
    boundaries = assignment.split('-')
    first = boundaries[0]
    second = boundaries[1]
    return list(range(int(first), int(second) + 1))


def parse_cleanup_pair(line):
    assignments = line.split(',')
    if len(assignments) != 2:
        raise ValueError('Schedule must contain exactly 2 assignments per line')

    first_cleaner = Cleaner(parse_assignment(assignments[0]))
    second_cleaner = Cleaner(parse_assignment(assignments[1]))

    return CleanerPair(first_cleaner, second_cleaner)


def read_cleanup_schedule(path):
    schedule = CleanupSchedule()

    with open(path) as file:
        for line in file:
            schedule.add_cleanup_pair(parse_cleanup_pair(line))

    return schedule