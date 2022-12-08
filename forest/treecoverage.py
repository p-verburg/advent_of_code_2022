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
        self.row_count = len(self.grid)
        self.col_count = len(self.grid[0])

    def is_higher(self, row, column, highest):
        height = self.grid[row][column].height
        if highest < height:
            highest = height
            self.grid[row][column].visible = True
        return highest

    def look_at_row(self, begin, end, step):
        for row in range(0, self.row_count):
            self.grid[row][begin].visible = True
            highest = self.grid[row][begin].height
            for col in range(begin + step, end + step, step):
                highest = self.is_higher(row, col, highest)

    def look_at_column(self, begin, end, step):
        for col in range(0, self.col_count):
            self.grid[begin][col].visible = True
            highest = self.grid[begin][col].height
            for row in range(begin + step, end + step, step):
                highest = self.is_higher(row, col, highest)

    def look_from_left(self):
        self.look_at_row(0, self.col_count - 1, 1)

    def look_from_right(self):
        self.look_at_row(self.col_count - 1, 0, -1)

    def look_from_above(self):
        self.look_at_column(0, self.row_count - 1, 1)

    def look_from_below(self):
        self.look_at_column(self.row_count - 1, 0, -1)

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

    def score_along_row(self, row, column, height, edge, direction):
        for c in range(column + direction, edge + direction, direction):
            if self.grid[row][c].height >= height:
                return direction * (c - column)
        return direction * (edge - column)

    def score_along_column(self, row, column, height, edge, direction):
        for r in range(row + direction, edge + direction, direction):
            if self.grid[r][column].height >= height:
                return direction * (r - row)
        return direction * (edge - row)

    def score_left(self, row, column, height):
        return self.score_along_row(row, column, height, 0, -1)

    def score_right(self, row, column, height):
        return self.score_along_row(row, column, height,
                                    self.col_count - 1, 1)

    def score_up(self, row, column, height):
        return self.score_along_column(row, column, height, 0, -1)

    def score_down(self, row, column, height):
        return self.score_along_column(row, column, height,
                                       self.row_count - 1, 1)

    def score(self, row, column):
        height = self.grid[row][column].height
        return self.score_left(row, column, height) \
            * self.score_right(row, column, height) \
            * self.score_up(row, column, height) \
            * self.score_down(row, column, height)
