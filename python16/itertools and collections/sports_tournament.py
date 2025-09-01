import itertools
from collections import Counter

teams = ["A", "B", "C", "D", "E"]

# Generate all matches
matches = list(itertools.combinations(teams, 2))
print("\n=== Sports Tournament ===")
for m in matches:
    print("Match:", m)

# Count appearances
count = Counter(itertools.chain.from_iterable(matches))
print("\nMatch Count per Team:", dict(count))

# Find most active team
top = count.most_common(1)[0]
print(f"\nMost Active Team: {top[0]} with {top[1]} matches")
