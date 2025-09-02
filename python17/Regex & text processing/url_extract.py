import re

html = """
Visit our site at https://example.com for details.
Our blog: http://blog.example.org
Secure login here: https://secure.shop.net/login
"""

pattern = r"https?://[a-zA-Z0-9./-]+"
urls = re.findall(pattern, html)

print("Extracted URLs:")
for url in urls:
    print(url)

print("Total URLs found:", len(urls))
