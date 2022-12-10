from communication.signal import Cpu, SignalSampler

cpu = Cpu()
sampler = SignalSampler(20, 40)
cpu.sampler = sampler

with open('program.txt') as file:
    cpu.start_program(file)

print(sum(sampler.samples))
