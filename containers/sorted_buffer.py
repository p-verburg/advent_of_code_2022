class SortedBuffer:
    def __init__(self, max_size):
        if max_size < 0:
            raise ValueError('max_size should be non-negative')

        self.max_size = max_size
        self.keys = []
        self.values = []

    def submit(self, key, value):
        if self.max_size == 0:
            return

        current_size = len(self.keys)

        for i in range(0, current_size):
            if key > self.keys[i]:
                self.insert(i, key, value)
                self.truncate()
                return

        if current_size < self.max_size:
            self.insert(current_size, key, value)

    def shift(self, start_index):
        current_size = len(self.keys)
        for i in range(current_size - 1, start_index, -1):
            self.keys[i] = self.keys[i-1]
            self.values[i] = self.values[i-1]

    def truncate(self, list=None):
        if not list:
            self.truncate(self.keys)
            self.truncate(self.values)
            return

        current_size = len(list)
        if current_size <= self.max_size:
            return

        for i in range(current_size - 1, self.max_size - 1, -1):
            del list[i]

    def insert(self, index, key, value):
        self.keys.insert(index, key)
        self.values.insert(index, value)
