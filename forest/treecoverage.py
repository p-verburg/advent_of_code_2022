class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False
        self.score = 0


class TreeMap:
    def __init__(self, grid):
        self.grid = grid
        for i in range(0, len(grid)):
            row = grid[i]
            for j in range(0, len(row)):
                row[j] = Tree(row[j])

    def count_visible(self):
        inspector = VisibilityInspector(self)
        inspector.inspect()

        count = 0
        for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[row])):
                if self.grid[row][col].visible:
                    count += 1
        return count

    def find_highest_scenic_score(self):
        scorer = ScenicScorer(self)

        highest_score = 0
        for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[row])):
                score = scorer.score(row, col)
                if score > highest_score:
                    highest_score = score
        return highest_score


class VisibilityInspector:
    def __init__(self, tree_map):
        self.grid = tree_map.grid

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

    def inspect(self):
        self.look_from_left()
        self.look_from_right()
        self.look_from_above()
        self.look_from_below()


class ScenicScorer:
    def __init__(self, tree_map):
        self.grid = tree_map.grid
        self.row_count = len(self.grid)
        self.col_count = len(self.grid[0])

    def score_left(self, row, column, height):
        for c in range(column - 1, -1, -1):
            if self.grid[row][c].height >= height:
                return column - c
        return column

    def score_right(self, row, column, height):
        for c in range(column + 1, self.col_count):
            if self.grid[row][c].height >= height:
                return c - column
        return self.col_count - 1 - column

    def score_up(self, row, column, height):
        for r in range(row - 1, -1, -1):
            if self.grid[r][column].height >= height:
                return row - r
        return row

    def score_down(self, row, column, height):
        for r in range(row + 1, self.row_count):
            if self.grid[r][column].height >= height:
                return r - row
        return self.row_count - 1 - row

    def score(self, row, column):
        height = self.grid[row][column].height
        return self.score_left(row, column, height) \
            * self.score_right(row, column, height) \
            * self.score_up(row, column, height) \
            * self.score_down(row, column, height)
