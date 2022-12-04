from campcleanup.schedule import read_cleanup_schedule

schedule = read_cleanup_schedule('cleanup_schedule.txt')

count = sum([1 for pair in schedule.pairs if pair.are_fully_overlapping()])

print(count)
