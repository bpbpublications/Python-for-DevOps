# Script: 011_find_fruit_names.py

# Importing the 're' module to work with regular expressions
import re

# Defining the pattern to match either 'apples' or 'oranges'
pattern = r"apples|oranges"

# Sample text in which to search for the pattern
text = "I like apples and oranges."

# Using re.findall() to find all occurrences of 'apples' or 'oranges' in the text
matches = re.findall(pattern, text)

# Printing the list of matched words
print("Matches:", matches)  # Output: ['apples', 'oranges']
