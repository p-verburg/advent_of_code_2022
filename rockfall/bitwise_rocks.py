import sys
from copy import deepcopy

from geometry.point import Point2D


class Rock:
    def __init__(self, shape):
        self.shape = shape
        self.height = len(self.shape)


class Dash(Rock):
    def __init__(self):
        super().__init__([
            0b00011110
        ])


class Plus(Rock):
    def __init__(self):
        super().__init__([
            0b00001000,
            0b00011100,
            0b00001000,
        ])


class Angle(Rock):
    def __init__(self):
        super().__init__([
            0b00011100,
            0b00000100,
            0b00000100,
        ])


class Pole(Rock):
    def __init__(self):
        super().__init__([
            0b00010000,
            0b00010000,
            0b00010000,
            0b00010000
        ])


class Square(Rock):
    def __init__(self):
        super().__init__([
            0b00011000,
            0b00011000
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


class Chamber:
    def __init__(self, jet_pattern):
        self.space = [0b11111111]
        self.highest_rock = 0
        self.jet_pattern = jet_pattern
        self.jet_pattern_length = len(self.jet_pattern)
        self.next_jet = 0

    def get_rock_height(self):
        return self.highest_rock

    def make_space_above(self, height):
        for _ in range(0, height):
            self.space.append(0b10000000)

    def get_next_jet(self):
        jet = self.jet_pattern[self.next_jet]
        self.next_jet += 1
        if self.next_jet == self.jet_pattern_length:
            self.next_jet = 0
        return jet

    def detect_right_collision(self, rock: Rock, position: Point2D):
        for dy in range(0, rock.height):
            y = position.y + dy
            if rock.shape[dy] & 0b00000001 or (rock.shape[dy] >> 1) & self.space[y]:
                return True
        return False

    def detect_left_collision(self, rock: Rock, position: Point2D):
        for dy in range(0, rock.height):
            y = position.y + dy
            if (rock.shape[dy] << 1) & self.space[y]:
                return True
        return False

    def detect_bottom_collision(self, rock: Rock, position: Point2D):
        for dy in range(0, rock.height):
            y = position.y + dy - 1
            if rock.shape[dy] & self.space[y]:
                return True
        return False

    def get_new_position(self, rock: Rock, position: Point2D, jet: int):
        if jet > 0:
            if self.detect_right_collision(rock, position):
                return position
            for i in range(0, rock.height):
                rock.shape[i] = rock.shape[i] >> 1
        elif self.detect_left_collision(rock, position):
            return position
        else:
            for i in range(0, rock.height):
                rock.shape[i] = rock.shape[i] << 1

        return position + Point2D(jet, 0)

    def settle_rock(self, rock: Rock, position: Point2D):
        y = None
        for dy in range(0, rock.height):
            y = position.y + dy
            self.space[y] |= rock.shape[dy]
        if y > self.highest_rock:
            self.highest_rock = y

    def drop_rock(self, rock: Rock):
        empty_space = len(self.space) - self.highest_rock - 1
        required_space = 3 + rock.height - empty_space
        self.make_space_above(required_space)

        rock = deepcopy(rock)

        position = Point2D(2, self.highest_rock + 4)
        while True:
            jet = self.get_next_jet()
            position = self.get_new_position(rock, position, jet)
            if self.detect_bottom_collision(rock, position):
                break
            position += Point2D(0, -1)

        self.settle_rock(rock, position)


def print_chamber(chamber: Chamber):
    for row in reversed(chamber.space[1:]):
        sys.stdout.write('|')
        mask = 0b01000000
        while mask != 0b00000000:
            if row & mask:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
            mask = mask >> 1
        sys.stdout.write('|\n')
    print("+-------+")
