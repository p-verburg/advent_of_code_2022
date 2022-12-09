from rope.ropephysics import RopeTracker

rope_tracker = RopeTracker()

with open('moves.txt') as file:
    for line in file:
        words = line.split()
        if len(words) == 2:
            direction = words[0]
            range = int(words[1])
            if direction == 'R':
                rope_tracker.move_head(range, 0)
            elif direction == 'L':
                rope_tracker.move_head(-range, 0)
            elif direction == 'U':
                rope_tracker.move_head(0, range)
            elif direction == 'D':
                rope_tracker.move_head(0, -range)

count = rope_tracker.count_distinct_positions()

print(count)
