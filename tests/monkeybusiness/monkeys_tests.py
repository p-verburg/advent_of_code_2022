import unittest

from arithmetic.operation import Add, Multiply, Square
from monkeybusiness.monkeys import Monkey, MonkeyList, Targeter


def create_monkey_list():
    monkeys = MonkeyList()
    monkeys.add(Monkey(Multiply(19), Targeter(23, 2, 3), [79, 98]))
    monkeys.add(Monkey(Add(6), Targeter(19, 2, 0), [54, 65, 75, 74]))
    monkeys.add(Monkey(Square(), Targeter(13, 1, 3), [79, 60, 97]))
    monkeys.add(Monkey(Add(3), Targeter(17, 0, 1), [74]))

    return monkeys


class MonkeyTests(unittest.TestCase):
    def test_first_round(self):
        monkeys = create_monkey_list()

        for monkey in monkeys:
            monkey.inspect_items()

        self.assertListEqual([20, 23, 27, 26], list(monkeys[0].items))
        self.assertEqual(2, monkeys[0].items_inspected)
        self.assertListEqual([2080, 25, 167, 207, 401, 1046], list(monkeys[1].items))
        self.assertEqual(4, monkeys[1].items_inspected)
        self.assertListEqual([], list(monkeys[2].items))
        self.assertEqual(3, monkeys[2].items_inspected)
        self.assertListEqual([], list(monkeys[3].items))
        self.assertEqual(5, monkeys[3].items_inspected)

        self.assertEqual(20, monkeys.calculate_business(2))


if __name__ == '__main__':
    unittest.main()
