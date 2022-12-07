from filesystem.tree import get_root_directory


class DirectorySmallerThanVisitor:
    def __init__(self, max_size):
        self.max_size = max_size
        self.directories = []

    def visit(self, directory):
        if directory.total_size() <= self.max_size:
            self.directories.append(directory)


class SmallestDirectoryLargerThanVisitor:
    def __init__(self, size):
        self.size = size
        self.directory = None
        self.directory_size = None

    def visit(self, directory):
        directory_size = directory.total_size()
        if not self.directory \
                or self.size <= directory_size < self.directory_size:
            self.directory = directory
            self.directory_size = directory_size
            return


class Explorer:
    def __init__(self, root=None):
        if not root:
            self.root = get_root_directory()
        else:
            self.root = root
        self.current_directory = self.root

    def change_directory(self, name):
        if name == '/':
            self.current_directory = self.root
            return

        if name == '..':
            self.current_directory = self.current_directory.parent
            return

        for subdirectory in self.current_directory.subdirectories:
            if subdirectory.name == name:
                self.current_directory = subdirectory
                return

    def process_command(self, command, arguments):
        if command == 'cd':
            self.change_directory(arguments[0])
        elif command == 'ls':
            pass
        else:
            raise ValueError('Unknown command ' + command)

    def create_directory_content(self, content_list):
        for line in content_list:
            words = line.split()
            if words[0] == 'dir':
                self.current_directory.add_subdirectory(words[1])
            else:
                self.current_directory.add_file(words[1], int(words[0]))

    def build_file_system(self, command_log):
        self.current_directory = self.root

        content_list = []

        for line in command_log:
            words = line.split()
            if words[0] == '$':
                self.create_directory_content(content_list)
                content_list.clear()

                self.process_command(words[1], words[2:])
            else:
                content_list.append(line)

        self.create_directory_content(content_list)

    def find_directories_smaller_than(self, size):
        visitor = DirectorySmallerThanVisitor(size)
        self.root.accept(visitor)

        return visitor.directories

    def find_closest_larger_directory(self, size):
        visitor = SmallestDirectoryLargerThanVisitor(size)
        self.root.accept(visitor)

        return visitor.directory, visitor.directory_size
