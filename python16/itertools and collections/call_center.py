import itertools
from collections import defaultdict, Counter

agents = ["A1", "A2", "A3", "A4"]
shifts = ["Morning", "Evening", "Night"]

rotation = itertools.cycle(agents)
assignments = defaultdict(list)

print("\n=== Call Center Shift Rotation ===")
for day in range(1, 7):  # 6 days schedule
    for shift in shifts:
        agent = next(rotation)
        assignments[agent].append((day, shift))
        print(f"Day {day}: {shift} -> {agent}")

# Workload summary
print("\n--- Agent Workload ---")
shift_count = Counter({a: len(s) for a, s in assignments.items()})
for a, c in shift_count.items():
    print(f"{a} worked {c} shifts")

# Find agent with most shifts
busy = shift_count.most_common(1)[0]
print(f"\nBusiest Agent: {busy[0]} with {busy[1]} shifts")
