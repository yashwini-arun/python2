import itertools
from collections import Counter

chars = "abc"
password = "cab"
attempts = itertools.product(chars, repeat=3)
counter = Counter()

print("\n=== Password Cracking Simulation ===")
for attempt in attempts:
    guess = "".join(attempt)
    counter["tries"] += 1
    print("Trying:", guess)  # simulate attempt

    if guess == password:
        print(f"\n✅ Password found: {guess}")
        break

print(f"\nTotal Attempts: {counter['tries']}")
