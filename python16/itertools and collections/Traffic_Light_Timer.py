import itertools
from collections import deque

lights = ["Red", "Green", "Yellow"]
cycle = itertools.cycle(lights)
sequence = deque()

for i in range(9):  # simulate 9 changes
    sequence.append(next(cycle))

print("\n=== Traffic Light Simulation ===")
print("Cycle Sequence:", list(sequence))

# Check how many times each light appeared
count = {l: sequence.count(l) for l in lights}
print("Light Counts:", count)
