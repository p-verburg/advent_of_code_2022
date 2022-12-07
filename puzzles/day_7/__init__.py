from filesystem.explorer import Explorer
from filesystem.tree import sum_directory_sizes

explorer = Explorer()

with open('command_log.txt') as file:
    explorer.build_file_system(file)

small_directories = explorer.find_directories_smaller_than(100000)

total_size = sum_directory_sizes(small_directories)

print(total_size)

total_disk_space = 70000000
required_space = 30000000
space_available = total_disk_space - explorer.root.total_size()
space_needed = required_space - space_available

directory, size = explorer.find_closest_larger_directory(space_needed)

print(size)
