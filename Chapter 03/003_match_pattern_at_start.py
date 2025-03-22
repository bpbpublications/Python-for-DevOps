# Script: 003_match_pattern_at_start.py

# Importing the 're' module to work with regular expressions
import re

# Using re.match() to check if the string 'python' starts with 'py'
match = re.match('py', 'python')

# Checking if a match is found
if match:
    # If a match is found, print the matched string
    print("Match found:", match.group())
