from geometry.point import Point2D
from numpy import sign


class RopeTracker:
    def __init__(self, knot_count):
        self.knots = []
        for i in range(0, knot_count):
            self.knots.append(Point2D(0, 0))
        self.trail = [self.tail()]

    def head(self):
        return self.knots[0]

    def tail(self):
        return self.knots[-1]

    @staticmethod
    def is_close(distance):
        return abs(distance.x) <= 1 and abs(distance.y) <= 1

    def step_head(self, delta_x, delta_y):
        self.knots[0] = self.knots[0] + Point2D(delta_x, delta_y)
        for i in range(1, len(self.knots)):
            distance = self.knots[i-1] - self.knots[i]
            if not RopeTracker.is_close(distance):
                self.knots[i] = self.knots[i] + distance.unit()

        self.trail.append(self.tail())

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
