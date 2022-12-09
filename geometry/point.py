from numpy import sign


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return other.x == self.x and other.y == self.y
        elif isinstance(other, list) or isinstance(other, tuple):
            return other[0] == self.x and other[1] == self.y
        return False

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    def unit(self):
        return Point2D(sign(self.x), sign(self.y))
