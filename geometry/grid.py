import sys


class ExtendableGrid:
    def __init__(self, blank, outside):
        self.rows = []
        self.blank = blank
        self.outside = outside
        self.left = 0
        self.right = 0
        self.width = 0

    def __getitem__(self, item):
        return self.rows[item]

    def set_bounds(self, left, right):
        self.left = left
        self.right = right
        self.width = self.right - self.left + 1

    def extend_to(self, left, right):
        if self.width == 0:
            width = left - right + 1
            for i in range(0, len(self.rows)):
                self.rows[i] = [self.blank] * width
            self.set_bounds(left, right)
            return

        shift = max(self.left - left, 0)
        grow = max(right - self.right, 0)
        if shift > 0 or grow > 0:
            for i in range(0, len(self.rows)):
                if shift > 0:
                    self.rows[i] = [self.blank] * shift + self.rows[i]
                self.rows[i].extend([self.blank] * grow)
            self.set_bounds(self.left - shift, self.right + grow)
            assert(self.width == len(self.rows[0]))

    def convert_x(self, x):
        return x - self.left

    def get_value(self, x, y):
        x = self.convert_x(x)
        if x < 0 or x > self.width - 1:
            return self.outside
        if y >= len(self.rows):
            return self.outside
        return self.rows[y][x]

    def set_value(self, x, y, value):
        x = self.convert_x(x)
        self.rows[y][x] = value


def print_grid(grid, encoder):
    y = 0
    for row in grid.rows:
        sys.stdout.write(f'{y: >3} ')

        for value in row:
            sys.stdout.write(encoder.get_char(value))
        sys.stdout.write('\n')
        y += 1
    sys.stdout.flush()

