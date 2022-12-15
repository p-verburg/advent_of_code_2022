from geometry.grid import print_grid, ExtendableGrid, ValueEncoder
from geometry.point import Point2D, parse_int_point

EMPTY = 0
ROCK = 1
OUTSIDE = 2
REST = SAND = 3


class CaveMap(ExtendableGrid):
    def __init__(self):
        super().__init__(EMPTY, OUTSIDE)
        self.source = Point2D(500, -1)
        self.moves = [Point2D(0, 1), Point2D(-1, 1), Point2D(1, 1)]

    def add_wall(self, start: Point2D, end: Point2D):
        lowest = max(start.y, end.y)

        while lowest > len(self.rows) - 1:
            self.rows.append([EMPTY] * self.width)

        if start.x < end.x:
            self.extend_horizontal(start.x, end.x)
        else:
            self.extend_horizontal(end.x, start.x)

        direction = (end - start).unit()
        point = start
        while not point == end:
            self.set_terrain(point.x, point.y, ROCK)
            point += direction
        self.set_terrain(end.x, end.y, ROCK)

    def create_floor(self):
        height = len(self.rows)
        self.extend_horizontal(self.source.x - height - 2,
                               self.source.x + height + 2)
        self.rows.append([EMPTY] * self.width)
        self.rows.append([ROCK] * self.width)

    def get_terrain(self, x, y):
        return self.get_value(x, y)

    def set_terrain(self, x, y, terrain):
        self.set_value(x, y, terrain)

    def move_grain(self, position):
        for move in self.moves:
            new_position = position + move
            terrain = self.get_terrain(new_position.x, new_position.y)
            if terrain == EMPTY or terrain == OUTSIDE:
                return new_position, terrain

        return position, REST

    def drop_grain(self):
        result = EMPTY
        position = self.source
        while result == EMPTY:
            position, result = self.move_grain(position)
            if result == REST:
                self.set_terrain(position.x, position.y, REST)

        return position, result

    def drop_sand(self):
        top_position = self.source + Point2D(0, 1)
        grains_dropped = 0
        position = self.source
        while not position == top_position:
            position, result = self.drop_grain()
            grains_dropped += 1

        return grains_dropped


def build_map(lines):
    cave_map = CaveMap()
    for line in lines:
        vertices = line.split(" -> ")
        start = parse_int_point(vertices[0])
        for i in range(1, len(vertices)):
            end = parse_int_point(vertices[i])
            cave_map.add_wall(start, end)
            start = end

    cave_map.create_floor()

    return cave_map


class TerrainEncoder(ValueEncoder):
    def __init__(self):
        super().__init__({
            EMPTY: '.',
            ROCK: '#',
            SAND: 'o'
        }, '.')


def print_map(cave_map):
    return print_grid(cave_map, TerrainEncoder())
