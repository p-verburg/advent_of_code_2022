class Operation:
    def apply(self, value):
        return value


class Add(Operation):
    def __init__(self, value):
        self.value = value

    def apply(self, value):
        return value + self.value


class Multiply(Operation):
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def apply(self, value):
        return value * self.multiplier


class Square(Operation):
    def apply(self, value):
        return value * value


class Predicate:
    def evaluate(self, value):
        return True


class DivisibleBy(Predicate):
    def __init__(self, divisor):
        self.divisor = divisor

    def evaluate(self, value):
        return value % self.divisor == 0
