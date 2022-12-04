import unittest
from calories.calories import CalorieList
from calories.calories import Elf
from calories.calories import get_total_calories


def generate_elf(food):
    elf = Elf()
    elf.food = food
    return elf


def generate_test_list():
    list = CalorieList()
    list.elves.append(generate_elf([1000, 2000, 3000]))
    list.elves.append(generate_elf([4000]))
    list.elves.append(generate_elf([5000, 6000]))
    list.elves.append(generate_elf([7000, 8000, 9000]))
    list.elves.append(generate_elf([10000]))
    return list


class CaloriesTests(unittest.TestCase):
    def test_read_file(self):
        list = CalorieList('test_list.txt')

        self.assertEqual(len(list.elves), 5)

        fourth_elf = list.elves[3]
        self.assertEqual([7000, 8000, 9000], fourth_elf.food)

    def test_get_total_calories(self):
        list = generate_test_list()

        self.assertEqual(list.total_calories(3), 24000)

    def test_get_total_calories_non_existing(self):
        list = generate_test_list()

        index = len(list.elves) + 1

        self.assertEqual(list.total_calories(index), None)

    def test_get_elf_with_most_calories(self):
        list = generate_test_list()

        elves = list.elves_with_most_calories(1)

        self.assertEqual(len(elves), 1)
        self.assertEqual(elves[0].total_calories(), 24000)

    def test_get_elves_with_most_calories(self):
        list = generate_test_list()

        elves = list.elves_with_most_calories(3)

        self.assertEqual(len(elves), 3)
        self.assertEqual(elves[0].total_calories(), 24000)
        self.assertEqual(elves[1].total_calories(), 11000)
        self.assertEqual(elves[2].total_calories(), 10000)

    def test_total_calories_of_elves(self):
        list = generate_test_list()

        total_calories = get_total_calories(list.elves)

        self.assertEqual(total_calories, 55000)


if __name__ == '__main__':
    unittest.main()
