import sys

from geometry.point import Point2D


class Rock:
    def __init__(self, shape):
        self.shape = shape
        self.height = len(self.shape)
        self.width = max(len(row) for row in self.shape)
        self.bottom = self.calculate_bottom()

    def calculate_bottom(self):
        bottom = [self.height] * self.width
        for y in range(0, self.height):
            row = self.shape[y]
            for x in row:
                if y < bottom[x]:
                    bottom[x] = y
        return bottom

class Dash(Rock):
    def __init__(self):
        super().__init__([
            [0, 1, 2, 3]
        ])


class Plus(Rock):
    def __init__(self):
        super().__init__([
            [1], [0, 1, 2], [1]
        ])


class Angle(Rock):
    def __init__(self):
        super().__init__([
            [0, 1, 2], [2], [2]
        ])


class Pole(Rock):
    def __init__(self):
        super().__init__([
            [0], [0], [0], [0]
        ])


class Square(Rock):
    def __init__(self):
        super().__init__([
            [0, 1], [0, 1]
        ])


class Rockfall:
    def __init__(self):
        self.rocks = [Dash(), Plus(), Angle(), Pole(), Square()]
        self.rocks_length = len(self.rocks)
        self.next_rock = 0

    def get_next_rock(self):
        next_rock = self.rocks[self.next_rock]
        self.next_rock += 1
        if self.next_rock == self.rocks_length:
            self.next_rock = 0
        return next_rock


EMPTY = 0
ROCK = 1


class Chamber:
    def __init__(self, jet_pattern):
        self.width = 7
        self.space = []
        self.highest_rock = -1
        self.jet_pattern = jet_pattern
        self.jet_pattern_length = len(self.jet_pattern)
        self.next_jet = 0

    def make_space_above(self, height):
        for _ in range(0, height):
            self.space.append([EMPTY] * self.width)

    def get_next_jet(self):
        jet = self.jet_pattern[self.next_jet]
        self.next_jet += 1
        if self.next_jet == self.jet_pattern_length:
            self.next_jet = 0
        return jet

    def detect_right_collision(self, rock: Rock, position: Point2D):
        for dy in range(0, rock.height):
            y = position.y + dy
            x = position.x + rock.shape[dy][-1] + 1
            if x >= self.width or self.space[y][x] == ROCK:
                return True
        return False

    def detect_left_collision(self, rock: Rock, position: Point2D):
        for dy in range(0, rock.height):
            y = position.y + dy
            x = position.x + rock.shape[dy][0] - 1
            if x < 0 or self.space[y][x] == ROCK:
                return True
        return False

    def detect_bottom_collision(self, rock: Rock, position: Point2D):
        for dx in range(0, rock.width):
            x = position.x + dx
            y = position.y + rock.bottom[dx] - 1
            if y < 0 or self.space[y][x] == ROCK:
                return True
        return False

    def get_new_position(self, rock: Rock, position: Point2D, jet: int):
        if jet > 0:
            if self.detect_right_collision(rock, position):
                return position
        elif self.detect_left_collision(rock, position):
            return position

        return position + Point2D(jet, 0)

    def settle_rock(self, rock: Rock, position: Point2D):
        y = None
        for dy in range(0, rock.height):
            y = position.y + dy
            for dx in rock.shape[dy]:
                x = position.x + dx
                self.space[y][x] = ROCK
        if y > self.highest_rock:
            self.highest_rock = y

    def drop_rock(self, rock: Rock):
        empty_space = len(self.space) - self.highest_rock - 1
        required_space = 3 + rock.height - empty_space
        self.make_space_above(required_space)

        position = Point2D(2, self.highest_rock + 4)
        while True:
            jet = self.get_next_jet()
            position = self.get_new_position(rock, position, jet)
            if self.detect_bottom_collision(rock, position):
                break
            position += Point2D(0, -1)

        self.settle_rock(rock, position)


def print_chamber(chamber: Chamber):
    for row in reversed(chamber.space):
        sys.stdout.write('|')
        for point in row:
            if point == EMPTY:
                sys.stdout.write('.')
            elif point == ROCK:
                sys.stdout.write('#')
            else:
                sys.stdout.write('?')
        sys.stdout.write('|\n')
    print("+-------+")
