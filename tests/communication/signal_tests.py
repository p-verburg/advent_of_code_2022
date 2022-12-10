import unittest

from communication.signal import NoopCommand, Cpu, AddCommand, SignalSampler


class CpuTests(unittest.TestCase):
    def test_noop_command(self):
        cpu = Cpu()
        command = NoopCommand()
        self.assertEqual(False, command.completed)

        command.execute(cpu)

        self.assertEqual(True, command.completed)

    def test_add_command(self):
        cpu = Cpu()
        self.assertEqual(1, cpu.X)

        command = AddCommand(3)
        self.assertEqual(False, command.completed)

        command.execute(cpu)
        self.assertEqual(1, cpu.X)
        self.assertEqual(False, command.completed)

        command.execute(cpu)
        self.assertEqual(4, cpu.X)
        self.assertEqual(True, command.completed)

    def test_signal_sampler(self):
        sampler = SignalSampler(0, 3)
        cpu = Cpu()
        self.assertListEqual([], sampler.samples)

        (cpu.cycle, cpu.X) = (3, 5)
        sampler.sample(cpu)
        self.assertListEqual([15], sampler.samples)

        (cpu.cycle, cpu.X) = (4, 7)
        sampler.sample(cpu)
        self.assertListEqual([15], sampler.samples)

        (cpu.cycle, cpu.X) = (9, 2)
        sampler.sample(cpu)
        self.assertListEqual([15, 18], sampler.samples)

    def test_long_program(self):
        cpu = Cpu()
        sampler = SignalSampler(20, 40)
        cpu.sampler = sampler

        with open('test_program.txt') as file:
            cpu.start_program(file)

        self.assertEqual(13140, sum(sampler.samples))


if __name__ == '__main__':
    unittest.main()
