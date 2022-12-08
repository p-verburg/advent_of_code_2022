class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False


class TreeMap:
    def __init__(self, grid):
        self.grid = grid
        for i in range(0, len(grid)):
            row = grid[i]
            for j in range(0, len(row)):
                row[j] = Tree(row[j])

    def look_from_left(self):
        for row in range(0, len(self.grid)):
            begin = 0
            end = len(self.grid[row]) - 1
            self.grid[row][begin].visible = True
            highest_left = self.grid[row][begin].height
            for col in range(begin + 1, end + 1, 1):
                height = self.grid[row][col].height
                if highest_left < height:
                    highest_left = height
                    self.grid[row][col].visible = True

    def look_from_right(self):
        for row in range(0, len(self.grid)):
            begin = 0
            end = len(self.grid[row]) - 1
            self.grid[row][end].visible = True
            highest_right = self.grid[row][end].height
            for col in range(end - 1, begin - 1, -1):
                height = self.grid[row][col].height
                if highest_right < height:
                    highest_right = height
                    self.grid[row][col].visible = True

    def look_from_above(self):
        for col in range(0, len(self.grid[0])):
            begin = 0
            end = len(self.grid) - 1
            self.grid[begin][col].visible = True
            highest_above = self.grid[begin][col].height
            for row in range(begin + 1, end + 1, 1):
                height = self.grid[row][col].height
                if highest_above < height:
                    highest_above = height
                    self.grid[row][col].visible = True

    def look_from_below(self):
        for col in range(0, len(self.grid[0])):
            begin = 0
            end = len(self.grid) - 1
            self.grid[end][col].visible = True
            highest_below = self.grid[end][col].height
            for row in range(end - 1, begin - 1, -1):
                height = self.grid[row][col].height
                if highest_below < height:
                    highest_below = height
                    self.grid[row][col].visible = True

    def count_visible(self):
        self.look_from_left()
        self.look_from_right()
        self.look_from_above()
        self.look_from_below()

        count = 0
        for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[row])):
                if self.grid[row][col].visible:
                    count += 1
        return count
