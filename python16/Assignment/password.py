import itertools
import string
from collections import Counter

print("\n=== Password Generator ===")

# Take user input for password length
try:
    length = int(input("Enter password length (e.g., 4): "))
except ValueError:
    print("Invalid input. Using default length = 4")
    length = 4

# Allowed characters: letters + digits
chars = string.ascii_letters + string.digits

# Generate all possible passwords of given length
passwords = itertools.product(chars, repeat=length)

count = 0
samples = []
usage_counter = Counter()

for pwd in passwords:
    password = "".join(pwd)
    count += 1

    if count <= 20:       # Collect sample
        samples.append(password)

    if count <= 1000:     # Track frequency
        usage_counter.update(password)

# Show sample passwords
print("\nSample Passwords (first 20):")
for s in samples:
    print(s)

# Frequency stats
print("\nCharacter Frequency (first 1000 passwords):")
for char, freq in usage_counter.most_common(10):
    print(f"{char}: {freq} times")

print(f"\nTotal Possible Passwords of Length {length}: {len(chars) ** length}")
print(f"Characters considered: {len(chars)} (A-Z, a-z, 0-9)")
