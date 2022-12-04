from containers.sorted_buffer import SortedBuffer


class Elf:
    def __init__(self):
        self.food = []

    def add_food_item(self, calories):
        self.food.append(calories)

    def total_calories(self):
        return sum(self.food)


def get_total_calories(list_of_elves):
    total_calories = 0
    for elf in list_of_elves:
        total_calories += elf.total_calories()
    return total_calories


class CalorieList:
    def __init__(self, path=None):
        self.elves = []
        if path:
            self.read_file(path)

    def read_file(self, path):
        current_elf = Elf()
        with open(path) as file:
            for line in file:
                if not line.rstrip() and current_elf.food:
                    self.elves.append(current_elf)
                    current_elf = Elf()
                else:
                    current_elf.add_food_item(int(line))

        if current_elf.food:
            self.elves.append(current_elf)

    def total_calories(self, index):
        if len(self.elves) < index:
            return None
        return self.elves[index].total_calories()

    def elves_with_most_calories(self, number_of_elves):
        buffer = SortedBuffer(number_of_elves)
        for elf in self.elves:
            total_calories = elf.total_calories()
            buffer.submit(total_calories, elf)

        return buffer.values
