class NullSampler:
    def sample(self, cpu):
        pass


class SignalSampler:
    def __init__(self, start, interval):
        self.start = start
        self.interval = interval
        self.samples = []

    def sample(self, cpu):
        if (cpu.cycle - self.start) % self.interval == 0:
            self.samples.append(cpu.cycle * cpu.X)

