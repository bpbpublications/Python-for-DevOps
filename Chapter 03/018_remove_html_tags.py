# Script: 018_remove_html_tags.py

# Importing the 're' module to work with regular expressions
import re

# Sample HTML string to remove tags from
html = "<p>This is a <b>bold</b> text.</p>"

# Using re.sub() to remove all HTML tags from the string
# The pattern '<[^>]+>' matches any sequence of characters between '<' and '>'
text = re.sub(r"<[^>]+>", "", html)

# Printing the text after removing HTML tags
print("Text:", text)
