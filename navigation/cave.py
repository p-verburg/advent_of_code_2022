import sys

from geometry.point import Point2D, parse_int_point


EMPTY = 0
ROCK = 1
OUTSIDE = 2
REST = SAND = 3


class CaveMap:
    def __init__(self):
        self.rows = []
        self.left = 0
        self.right = 0
        self.width = 0
        self.moves = [Point2D(0, 1), Point2D(-1, 1), Point2D(1, 1)]

    def __getitem__(self, item):
        return self.rows[item]

    def set_bounds(self, left, right):
        self.left = left
        self.right = right
        self.width = self.right - self.left + 1

    def add_wall(self, start: Point2D, end: Point2D):
        lowest = max(start.y, end.y)

        while lowest > len(self.rows) - 1:
            self.rows.append([EMPTY] * self.width)

        if start.x < end.x:
            self.extend_to(start.x, end.x)
        else:
            self.extend_to(end.x, start.x)

        direction = (end - start).unit()
        point = start
        while not point == end:
            self.set_terrain(point.x, point.y, ROCK)
            point += direction
        self.set_terrain(end.x, end.y, ROCK)

    def extend_to(self, left, right):
        if self.width == 0:
            width = left - right + 1
            for i in range(0, len(self.rows)):
                self.rows[i] = [EMPTY] * width
            self.set_bounds(left, right)
            return

        shift = max(self.left - left, 0)
        grow = max(right - self.right, 0)
        if shift > 0 or grow > 0:
            for i in range(0, len(self.rows)):
                if shift > 0:
                    self.rows[i] = [EMPTY] * shift + self.rows[i]
                self.rows[i].extend([EMPTY] * grow)
            self.set_bounds(self.left - shift, self.right + grow)
            assert(self.width == len(self.rows[0]))

    def convert_x(self, x):
        return x - self.left

    def get_terrain(self, x, y):
        x = self.convert_x(x)
        if x < 0 or x > self.width - 1:
            return OUTSIDE
        if y >= len(self.rows):
            return OUTSIDE
        return self.rows[y][x]

    def set_terrain(self, x, y, terrain):
        x = self.convert_x(x)
        self.rows[y][x] = terrain

    def move_grain(self, position):
        for move in self.moves:
            new_position = position + move
            terrain = self.get_terrain(new_position.x, new_position.y)
            if terrain == EMPTY or terrain == OUTSIDE:
                return new_position, terrain

        return position, REST

    def drop_grain(self):
        result = EMPTY
        position = Point2D(500, 0)
        while result == EMPTY:
            position, result = self.move_grain(position)
            if result == OUTSIDE:
                return OUTSIDE
            if result == REST:
                self.set_terrain(position.x, position.y, REST)
                return REST

    def drop_sand(self):
        grains_dropped = 0
        result = EMPTY
        while not result == OUTSIDE:
            result = self.drop_grain()
            grains_dropped += 1

        return grains_dropped - 1


def build_map(lines):
    cave_map = CaveMap()
    for line in lines:
        vertices = line.split(" -> ")
        start = parse_int_point(vertices[0])
        for i in range(1, len(vertices)):
            end = parse_int_point(vertices[i])
            cave_map.add_wall(start, end)
            start = end

    return cave_map


def print_map(cave_map):
    y = 0
    for row in cave_map.rows:
        sys.stdout.write(f'{y: >3} ')

        for terrain in row:
            char = '.'
            if terrain == EMPTY:
                char = '.'
            elif terrain == ROCK:
                char = '#'
            elif terrain == SAND:
                char = 'o'

            sys.stdout.write(char)
        sys.stdout.write('\n')
        y += 1
    sys.stdout.flush()
