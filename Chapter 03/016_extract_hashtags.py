# Script: 016_extract_hashtags.py

# Importing the 're' module to work with regular expressions
import re

# Sample post containing hashtags
post = "Loving the #sunny weather in #California"

# Using re.findall() to find all hashtags in the post
# The pattern '#(\w+)' matches a hashtag followed by one or more word characters (letters, digits, or underscores)
hashtags = re.findall(r"#(\w+)", post)

# Printing the list of hashtags found in the post
print("Hashtags:", hashtags)
