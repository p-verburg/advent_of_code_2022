import sys


class ExtendableGrid:
    def __init__(self, blank, outside):
        self.rows = []
        self.blank = blank
        self.outside = outside
        self.left = 0
        self.right = 0
        self.width = 0
        self.top = 0
        self.bottom = 0
        self.height = 0

    def __getitem__(self, item):
        return self.rows[self.convert_y(item)]

    def set_horizontal_bounds(self, left, right):
        self.left = left
        self.right = right
        self.width = self.right - self.left + 1

    def set_vertical_bounds(self, top, bottom):
        self.top = top
        self.bottom = bottom
        self.height = self.bottom - self.top + 1

    def convert_x(self, x):
        return x - self.left

    def convert_y(self, y):
        return y - self.top

    def set_value(self, x, y, value):
        x = self.convert_x(x)
        y = self.convert_y(y)
        self.rows[y][x] = value

    def get_value(self, x, y):
        x = self.convert_x(x)
        if x < 0 or x >= self.width:
            return self.outside
        y = self.convert_y(y)
        if y < 0 or y >= len(self.rows):
            return self.outside
        return self.rows[y][x]

    def extend_horizontal(self, left, right):
        if self.width == 0:
            width = left - right + 1
            for i in range(0, len(self.rows)):
                self.rows[i] = [self.blank] * width
            self.set_horizontal_bounds(left, right)
            return

        shift = max(self.left - left, 0)
        grow = max(right - self.right, 0)
        if shift > 0 or grow > 0:
            for i in range(0, len(self.rows)):
                if shift > 0:
                    self.rows[i] = [self.blank] * shift + self.rows[i]
                self.rows[i].extend([self.blank] * grow)
            self.set_horizontal_bounds(self.left - shift, self.right + grow)

            assert(self.width == len(self.rows[0]))

    def extend_vertical(self, top, bottom):
        if len(self.rows) == 0:
            height = bottom - top + 1
            self.rows = [[self.blank] * self.width] * height
            self.top = top
            self.bottom = bottom
            self.height = height
            return

        shift = max(self.top - top, 0)
        if shift > 0:
            self.rows = [[self.blank] * self.width] * shift + self.rows

        grow = max(bottom - self.bottom, 0)
        if grow > 0:
            self.rows.extend([[self.blank] * self.width] * grow)

        self.set_vertical_bounds(self.top - shift, self.bottom + grow)

        assert(self.height == len(self.rows))


def print_grid(grid, encoder):
    y = 0
    for row in grid.rows:
        sys.stdout.write(f'{y: >3} ')

        for value in row:
            sys.stdout.write(encoder.get_char(value))
        sys.stdout.write('\n')
        y += 1
    sys.stdout.flush()
