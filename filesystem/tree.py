class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __eq__(self, other):
        return self.name == other.name \
               and self.size == other.size


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirectories = []
        self.files = []

    def add_subdirectory(self, name):
        subdirectory = Directory(name, self)
        self.subdirectories.append(subdirectory)
        return subdirectory

    def add_file(self, name, size):
        file = File(name, size)
        self.files.append(file)
        return file

    def total_size(self):
        total_size = 0
        for subdirectory in self.subdirectories:
            total_size += subdirectory.total_size()
        for file in self.files:
            total_size += file.size
        return total_size

    def accept(self, visitor):
        visitor.visit(self)
        for subdirectory in self.subdirectories:
            subdirectory.accept(visitor)


def get_root_directory():
    return Directory('/', None)


def sum_directory_sizes(directories):
    total_size = 0
    for directory in directories:
        total_size += directory.total_size()
    return total_size
