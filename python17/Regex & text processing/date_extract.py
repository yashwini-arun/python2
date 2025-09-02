import re

# Sample text with dates
text = """
The meeting is on 01-09-2025.
Project deadline: 2025/09/15.
Next event: Sept 20, 2025.
"""

# Regex to capture different date formats
pattern = r"(\d{2}-\d{2}-\d{4}|\d{4}/\d{2}/\d{2}|[A-Za-z]{3,9}\s\d{1,2},\s\d{4})"

dates = re.findall(pattern, text)

print("Dates Found:")
for d in dates:
    print(d)
