from calories.calories import CalorieList
from calories.calories import get_total_calories

list = CalorieList('calories_list.txt')

elves = list.elves_with_most_calories(3)

total = get_total_calories(elves)

print(total)
