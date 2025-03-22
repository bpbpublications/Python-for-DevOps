# Script: 020_split_text_by_multiple_delimiters.py

# Importing the 're' module to work with regular expressions
import re

# Sample text containing items separated by commas, semicolons, and spaces
text = "apple, banana; orange"

# Using re.split() to split the text by one or more occurrences of commas, semicolons, or spaces
# The pattern '[,; ]+' matches any combination of commas, semicolons, or spaces as delimiters
items = re.split(r"[,; ]+", text)

# Printing the list of items after splitting the text
print("Items:", items)
