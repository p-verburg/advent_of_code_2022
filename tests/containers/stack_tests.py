import unittest
from containers.stack import Stack


def create_stack_of(stack_size):
    stack = Stack()
    for i in range(1, stack_size+1):
        stack.push(i)
    return stack


class StackTests(unittest.TestCase):
    def test_push_three(self):
        stack = Stack()

        stack.push(1)
        stack.push(4)
        stack.push(7)

        self.assertEqual(len(stack), 3)

    def test_peek(self):
        stack = create_stack_of(3)

        self.assertEqual(stack.peek(), 3)
        self.assertEqual(len(stack), 3)

    def test_pop_one(self):
        stack = create_stack_of(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(len(stack), 2)

    def test_pop_two(self):
        stack = create_stack_of(3)
        stack.pop()

        self.assertEqual(stack.pop(), 2)
        self.assertEqual(len(stack), 1)

    def test_prepend_three(self):
        stack = Stack()
        stack.prepend(4)
        stack.prepend(5)
        stack.prepend(6)

        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 6)


if __name__ == '__main__':
    unittest.main()
