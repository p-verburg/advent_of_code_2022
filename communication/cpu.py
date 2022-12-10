from communication.screen import Screen
from communication.signalsampler import NullSampler


class NoopCommand:
    def __init__(self):
        self.completed = False

    def execute(self, cpu):
        self.completed = True


class AddCommand:
    def __init__(self, value):
        self.value = value
        self.duration = 2
        self.completed = False

    def execute(self, cpu):
        if self.completed:
            return
        self.duration -= 1
        if self.duration == 0:
            cpu.X += self.value
            self.completed = True
        return


class Cpu:
    def __init__(self):
        self.cycle = 0
        self.X = 1
        self.sampler = NullSampler()
        self.screen = Screen(self)

    def parse_command(self, instruction):
        words = instruction.split()
        if words[0] == 'addx':
            return AddCommand(int(words[1]))
        return NoopCommand()

    def start_program(self, program):
        for instruction in program:
            command = self.parse_command(instruction)
            while not command.completed:
                self.cycle += 1
                self.sampler.sample(self)
                self.screen.draw_pixel()
                command.execute(self)

