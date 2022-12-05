import unittest
from packing.crates import Move, read_cargo_stacks, read_moves, read_cargo_file, move_9000, move_9001


class CargoStacksTests(unittest.TestCase):
    def test_read_stacks(self):
        with open('cargo_test_file.txt') as file:
            stacks = read_cargo_stacks(file)

        self.assertEqual(3, len(stacks))
        self.assertEqual(2, len(stacks[0]))
        self.assertEqual('N', stacks[0].pop())
        self.assertEqual('Z', stacks[0].pop())
        self.assertEqual(3, len(stacks[1]))
        self.assertEqual('D', stacks[1].pop())
        self.assertEqual('C', stacks[1].pop())
        self.assertEqual('M', stacks[1].pop())
        self.assertEqual(1, len(stacks[2]))
        self.assertEqual('P', stacks[2].pop())

    def test_read_moves(self):
        skip_lines = 5
        with open('cargo_test_file.txt') as file:
            for _ in range(skip_lines):
                next(file)
            moves = read_moves(file)

        self.assertEqual(4, len(moves))
        self.assertEqual(Move(1, 2, 1), moves[0])
        self.assertEqual(Move(3, 1, 3), moves[1])
        self.assertEqual(Move(2, 2, 1), moves[2])
        self.assertEqual(Move(1, 1, 2), moves[3])

    def test_move_crates_9000(self):
        stacks, moves = read_cargo_file('cargo_test_file.txt')

        for move in moves:
            move_9000(stacks, move)

        self.assertEqual(1, len(stacks[0]))
        self.assertEqual('C', stacks[0].pop())
        self.assertEqual(1, len(stacks[1]))
        self.assertEqual('M', stacks[1].pop())
        self.assertEqual(4, len(stacks[2]))
        self.assertEqual('Z', stacks[2].pop())
        self.assertEqual('N', stacks[2].pop())
        self.assertEqual('D', stacks[2].pop())
        self.assertEqual('P', stacks[2].pop())

    def test_move_crates_9001(self):
        stacks, moves = read_cargo_file('cargo_test_file.txt')

        for move in moves:
            move_9001(stacks, move)

        self.assertEqual(1, len(stacks[0]))
        self.assertEqual('M', stacks[0].pop())
        self.assertEqual(1, len(stacks[1]))
        self.assertEqual('C', stacks[1].pop())
        self.assertEqual(4, len(stacks[2]))
        self.assertEqual('D', stacks[2].pop())
        self.assertEqual('N', stacks[2].pop())
        self.assertEqual('Z', stacks[2].pop())
        self.assertEqual('P', stacks[2].pop())


if __name__ == '__main__':
    unittest.main()
