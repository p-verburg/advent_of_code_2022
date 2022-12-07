from filesystem.explorer import Explorer
from filesystem.tree import sum_directory_sizes

explorer = Explorer()

with open('command_log.txt') as file:
    explorer.build_file_system(file)

small_directories = explorer.find_directories_smaller_than(100000)

total_size = sum_directory_sizes(small_directories)

print(total_size)
