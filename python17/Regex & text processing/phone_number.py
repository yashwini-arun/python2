import re

# Sample text with phone numbers
text = """
Call me at 987-654-3210 or (080) 22334455.
Emergency: +91 9988776655.
"""

# Regex for phone numbers
pattern = r"(\+91\s\d{10}|\(\d{3}\)\s?\d{8}|\d{3}-\d{3}-\d{4})"

numbers = re.findall(pattern, text)

print("Phone Numbers Found:")
for num in numbers:
    print(num)
