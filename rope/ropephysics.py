from geometry.point import Point2D
from numpy import sign


class RopeTracker:
    def __init__(self):
        self.head = Point2D(0, 0)
        self.tail = Point2D(0, 0)
        self.trail = [self.tail]

    @staticmethod
    def is_small_enough(distance):
        return abs(distance.x) <= 1 and abs(distance.y) <= 1

    def step_head(self, delta_x, delta_y):
        self.head = self.head + Point2D(delta_x, delta_y)
        distance = self.head - self.tail
        if not RopeTracker.is_small_enough(distance):
            self.tail = self.tail + (self.head - self.tail).unit()
            self.trail.append(self.tail)

    def move_head(self, delta_x, delta_y):
        if delta_y == 0:
            for _ in range(0, abs(delta_x)):
                self.step_head(sign(delta_x), 0)
        elif delta_x == 0:
            for _ in range(0, abs(delta_y)):
                self.step_head(0, sign(delta_y))
        else:
            raise ValueError('Head move may only be horizontal or vertical')

    def count_distinct_positions(self):
        unique_positions = set(self.trail)
        return len(unique_positions)
