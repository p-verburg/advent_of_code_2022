import sys


class Screen:
    def __init__(self, cpu):
        self.cpu = cpu

    def draw_pixel(self):
        pixel = '.'
        draw_position = (self.cpu.cycle - 1) % 40
        if draw_position == self.cpu.X + 1 \
                or draw_position == self.cpu.X \
                or draw_position == self.cpu.X - 1:
            pixel = '#'

        sys.stdout.write(pixel)
        if self.cpu.cycle % 40 == 0:
            sys.stdout.write('\n')
            sys.stdout.flush()

    def draw(self):
        pass
