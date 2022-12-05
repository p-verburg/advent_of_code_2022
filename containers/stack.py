import copy


class Stack:
    def __init__(self):
        self.list = []

    def __deepcopy__(self, memo):
        stack = Stack()
        stack.list = copy.deepcopy(self.list, memo)
        return stack

    def __len__(self):
        return len(self.list)

    def push(self, element):
        self.list.append(element)

    def prepend(self, element):
        self.list.insert(0, element)

    def pop(self):
        element = self.list[-1]
        del self.list[-1]
        return element

    def peek(self):
        return self.list[-1]
