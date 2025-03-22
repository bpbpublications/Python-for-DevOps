# Script: 008_search_and_group_pattern.py

# Importing the 're' module to work with regular expressions
import re

# Using re.search() to search for the pattern with two groups: 'py' and 'thon' in the string 'python'
match = re.search(r'(py)(thon)', 'python')

# Checking if a match is found
if match:
    # Printing the whole matched string (group 0)
    print("Whole match:", match.group(0))  # Output: python
    
    # Printing the first captured group (group 1)
    print("First group:", match.group(1))  # Output: py
    
    # Printing the second captured group (group 2)
    print("Second group:", match.group(2)) # Output: thon
