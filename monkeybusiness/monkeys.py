from collections import deque
from arithmetic.operation import DivisibleBy
from containers.sorted_buffer import SortedBuffer


class Targeter(DivisibleBy):
    def __init__(self, divisor, match, other):
        super().__init__(divisor)
        self.match_target = match
        self.other_target = other

    def choose_target(self, value):
        if self.evaluate(value):
            return self.match_target
        else:
            return self.other_target


class Monkey:
    def __init__(self, worry, targeter, items):
        self.items = deque(items)
        self.more_worry = worry
        self.targeter = targeter
        self.monkeys = MonkeyList()
        self.items_inspected = 0
        self.super_divisor = 1

    def catch_item(self, item):
        self.items.append(item)

    def throw_to(self, item, monkey):
        monkey.catch_item(item)

    def throw_item(self, item):
        item = item % self.super_divisor
        target_index = self.targeter.choose_target(item)
        self.throw_to(item, self.monkeys[target_index])

    def inspect_items(self):
        item_count = len(self.items)

        if self.monkeys.reduce_worry:
            for _ in range(0, item_count):
                item = self.items.popleft()
                item = self.more_worry.apply(item)
                self.items_inspected += 1
                item = int(self.monkeys.reduce_worry.apply(item))
                self.throw_item(item)
        else:
            for _ in range(0, item_count):
                item = self.items.popleft()
                item = self.more_worry.apply(item)
                self.items_inspected += 1
                self.throw_item(item)


class MonkeyList:
    def __init__(self):
        self.monkeys = []
        self.current = -1
        self.reduce_worry = None

    def __getitem__(self, item):
        return self.monkeys[item]

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.monkeys):
            return self.monkeys[self.current]
        raise StopIteration

    def add(self, monkey):
        monkey.monkeys = self
        self.monkeys.append(monkey)
        return self.monkeys[-1]

    def calculate_super_divisor(self):
        divisor = 1
        for monkey in self.monkeys:
            divisor *= monkey.targeter.divisor
        return divisor

    def set_super_divisor(self):
        divisor = self.calculate_super_divisor()
        for monkey in self.monkeys:
            monkey.super_divisor = divisor

    def calculate_business(self, count):
        most_active = SortedBuffer(2)
        for monkey in self.monkeys:
            most_active.submit(monkey.items_inspected, monkey)

        business = 1
        for key in most_active.keys:
            business *= key

        return business
