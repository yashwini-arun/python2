import re

tweets = """
Loving the new phone! #technology #gadgets
Weekend vibes are the best. #relax #fun
Work hard, play harder! #motivation #life
"""

pattern = r"#\w+"
hashtags = re.findall(pattern, tweets)

print("Extracted Hashtags:")
for h in hashtags:
    print(h)

print("Unique Hashtags:", set(hashtags))
