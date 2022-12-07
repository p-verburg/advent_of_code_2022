class DirectorySmallerThanVisitor:
    def __init__(self, max_size):
        self.max_size = max_size
        self.directories = []

    def visit(self, directory):
        if directory.total_size() <= self.max_size:
            self.directories.append(directory)


class Explorer:
    def __init__(self, start_directory):
        self.start = start_directory

    def find_directories_smaller_than(self, size):
        visitor = DirectorySmallerThanVisitor(size)
        self.start.accept(visitor)

        return visitor.directories
