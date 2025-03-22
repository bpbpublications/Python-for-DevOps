# Script: 009_greedy_vs_non_greedy_match.py

# Importing the 're' module to work with regular expressions
import re

# Using a greedy match to capture everything between '<' and '>'
# The greedy match will capture the longest possible string that matches the pattern
greedy_match = re.search(r'<.*>', '<a> <b>').group()

# Using a non-greedy match to capture everything between '<' and '>'
# The non-greedy match will capture the shortest possible string that matches the pattern
non_greedy_match = re.search(r'<.*?>', '<a> <b>').group()

# Printing the greedy match result
print("Greedy match:", greedy_match)       # Output: <a> <b>

# Printing the non-greedy match result
print("Non-greedy match:", non_greedy_match) # Output: <a>
