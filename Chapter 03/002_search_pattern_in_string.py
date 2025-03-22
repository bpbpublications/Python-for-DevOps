# Script: 002_search_pattern_in_string.py

# Importing the 're' module to work with regular expressions
import re

# Using re.search() to search for the pattern 'p..n' in the string 'python'
# The pattern 'p..n' matches the character 'p', followed by any two characters, and ending with 'n'
match = re.search('p..n', 'python')

# Checking if a match is found
if match:
    # If a match is found, print the matched string
    print("Match found:", match.group())
else:
    # If no match is found, print a message indicating no match
    print("No match found")
