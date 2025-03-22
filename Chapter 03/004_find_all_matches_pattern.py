# Script: 004_find_all_matches_pattern.py

# Importing the 're' module to work with regular expressions
import re

# Using re.findall() to find all substrings that match the pattern 'p..'
# The pattern 'p..' matches the character 'p' followed by any two characters
all_matches = re.findall('p..', 'python and pylon')

# Printing all the matches found in the string
print("Matches found:", all_matches)
