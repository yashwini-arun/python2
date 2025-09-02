import re  

# Sample raw text with emails and phone numbers
text = """
Hello, please contact us at john.doe@example.com or jane_smith123@test.org. 
For urgent queries, reach admin@company.co.in. 
You can call us at +1-987-654-3210 or (123) 456-7890. 
Alternate number: 9876543210
"""

# Regex for emails
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Regex for phone numbers (handles multiple formats)
phone_pattern = r"(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})"

# Extract emails
emails = re.findall(email_pattern, text)

# Extract phone numbers
phones = re.findall(phone_pattern, text)

# Print emails
print("=== Extracted Emails ===")
for email in emails:
    print(email)

# Print phone numbers (join groups into full number)
print("\n=== Extracted Phone Numbers ===")
for phone in phones:
    full_number = "".join(phone)
    print(full_number)
