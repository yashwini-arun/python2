import itertools
from collections import deque, Counter

# List of flights and runways
flights = ["F101", "F202", "F303", "F404", "F505"]
runways = ["R1", "R2"]

# Generate all possible (flight, runway) pairings
schedule = deque(itertools.product(flights, runways))

# Track runway usage
usage = Counter()

print("Airport Runway Allocation:\n" + "-"*30)
while schedule:
    flight, runway = schedule.popleft()
    usage[runway] += 1
    print(f"Flight {flight} -> Runway {runway}")
    # Limit to 2 flights per runway for demo
    if usage[runway] >= 2:
        print(f"Runway {runway} reached capacity.")
        continue

print("\nRunway Usage Summary:")
for r, c in usage.items():
    print(f"{r}: {c} flights handled")
