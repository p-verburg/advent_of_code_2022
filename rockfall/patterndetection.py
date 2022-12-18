from copy import deepcopy

from rockfall.bitwise_rocks import Chamber, Rockfall


class Pattern:
    def __init__(self, height, number_of_rocks):
        self.height = height
        self.number_of_rocks = number_of_rocks


def detect_pattern(chamber: Chamber, min_pattern_height):
    pattern_height = min_pattern_height
    rock_height = chamber.get_rock_height()
    while 3*pattern_height < rock_height:
        last_chunk = chamber.space[-2*pattern_height:-pattern_height]
        next_chunk = chamber.space[-3*pattern_height:-2*pattern_height]
        if last_chunk == next_chunk:
            return pattern_height
        pattern_height += 1

    return None


def count_rocks_in_pattern(chamber: Chamber, rockfall: Rockfall, pattern_height):
    start_rock_count = rockfall.rocks_dropped
    start_height = chamber.get_rock_height()
    added_height = 0
    top_pattern = deepcopy(chamber.space[-pattern_height:])
    while added_height != pattern_height:
        chamber.drop_rock(rockfall.get_next_rock())
        added_height = chamber.get_rock_height() - start_height

    while chamber.space[-pattern_height:] != top_pattern:
        chamber.drop_rock(rockfall.get_next_rock())

    return rockfall.rocks_dropped - start_rock_count


def predict_height(chamber: Chamber, min_pattern_height, target_rock_count):
    rockfall = Rockfall()
    for _ in range(4*min_pattern_height):
        chamber.drop_rock(rockfall.get_next_rock())

    pattern_height = detect_pattern(chamber, min_pattern_height)
    if not pattern_height:
        return None
    pattern_rock_count = count_rocks_in_pattern(chamber, rockfall, pattern_height)

    start_rock_count = rockfall.rocks_dropped
    rocks_to_go = target_rock_count - start_rock_count

    patterns_to_add = int(rocks_to_go / pattern_rock_count)
    height_to_add = patterns_to_add * pattern_height

    rocks_to_go = rocks_to_go % pattern_rock_count

    for _ in range(0, rocks_to_go):
        chamber.drop_rock(rockfall.get_next_rock())

    assert(rockfall.rocks_dropped == start_rock_count + rocks_to_go)
    assert(rockfall.rocks_dropped + pattern_rock_count * patterns_to_add == target_rock_count)

    return chamber.get_rock_height() + height_to_add
