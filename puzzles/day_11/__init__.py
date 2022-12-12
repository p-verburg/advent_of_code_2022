from monkeybusiness.monkeys import Monkey, MonkeyList, Targeter
from arithmetic.operation import Add, Multiply, Square, Divide


def create_monkey_list():
    monkeys = MonkeyList()
    monkeys.add(Monkey(Multiply(13), Targeter(5, 1, 6), [52, 78, 79, 63, 51, 94]))
    monkeys.add(Monkey(Add(3), Targeter(7, 5, 3), [77, 94, 70, 83, 53]))
    monkeys.add(Monkey(Square(), Targeter(13, 0, 6), [98, 50, 76]))
    monkeys.add(Monkey(Add(5), Targeter(11, 5, 7), [92, 91, 61, 75, 99, 63, 84, 69]))
    monkeys.add(Monkey(Add(7), Targeter(3, 2, 0), [51, 53, 83, 52]))
    monkeys.add(Monkey(Add(4), Targeter(2, 4, 7), [76, 76]))
    monkeys.add(Monkey(Multiply(19), Targeter(17, 1, 3), [75, 59, 93, 69, 76, 96, 65]))
    monkeys.add(Monkey(Add(2), Targeter(19, 2, 4), [89]))
    return monkeys


monkeys = create_monkey_list()
monkeys.reduce_worry = Divide(3)
for _ in range(0, 20):
    for monkey in monkeys:
        monkey.inspect_items()

print(monkeys.calculate_business(2))

monkeys = create_monkey_list()
monkeys.set_super_divisor()
for _ in range(0, 10_000):
    for monkey in monkeys:
        monkey.inspect_items()

print(monkeys.calculate_business(2))
