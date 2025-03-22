# Script: 022_find_capitalized_words.py

# Importing the 're' module to work with regular expressions
import re

# Sample text to find capitalized words
text = "London is the Capital of England."

# Using re.findall() to find all capitalized words in the text
# The pattern '\b[A-Z][a-z]*\b' matches words that start with an uppercase letter followed by lowercase letters
capitalized_words = re.findall(r"\b[A-Z][a-z]*\b", text)

# Printing the list of capitalized words found in the text
print("Capitalized words:", capitalized_words)
