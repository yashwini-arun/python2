import re

sample_text = """
John Doe
Email: john.doe123@gmail.com
Alternate: johndoe@company.org
Phone: +91-9876543210
Email: recruiter@jobs.in
"""

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(pattern, sample_text)

print("=== Extracted Emails ===")
for e in emails:
    print(e)

print("\nTotal Emails Found:", len(emails))
print("=== End of Email Extraction ===")