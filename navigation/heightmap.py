from geometry.point import Point2D


class HeightMap:
    def __init__(self, lines):
        self.map = []
        self.start = None
        self.end = None
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                break
            self.map.append([])
            row = self.map[-1]
            for char in line:
                if char == 'S':
                    self.start = Point2D(len(row), len(self.map) - 1)
                    char = 'a'
                elif char == 'E':
                    self.end = Point2D(len(row), len(self.map) - 1)
                    char = 'z'
                row.append(ord(char) - ord('a'))
        self.width = len(self.map[0])
        self.height = len(self.map)

    def __getitem__(self, item):
        return self.map[item]


def read_map(path):
    with open(path) as file:
        return HeightMap(file)


def find_shortest_path(height_map):
    visited = [height_map.end]
    paths = [[height_map.end]]
    map_size = height_map.width * height_map.height

    directions = [Point2D(-1, 0), Point2D(0, 1), Point2D(1, 0), Point2D(0, -1)]
    steps = 0
    while True:
        new_paths = []
        for path in paths:
            last_point = path[-1]
            last_height = height_map[last_point.y][last_point.x]
            for direction in directions:
                next_point = last_point + direction
                if next_point in visited:
                    continue
                if next_point.x < 0 or next_point.x >= height_map.width \
                        or next_point.y < 0 or next_point.y >= height_map.height:
                    continue
                next_height = height_map[next_point.y][next_point.x]
                if last_height - next_height <= 1:
                    new_path = path.copy()
                    new_path.append(next_point)
                    if next_point == height_map.start:
                        return new_path
                    visited.append(next_point)
                    new_paths.append(new_path)

        steps += 1
        if steps >= map_size:
            return None
        if len(visited) == map_size:
            return None

        paths = new_paths
