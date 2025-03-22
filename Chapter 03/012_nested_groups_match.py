# Script: 012_nested_groups_match.py

# Importing the 're' module to work with regular expressions
import re

# Defining a pattern with nested groups: '(a(b)c)'
# The outer group captures 'abc', while the inner group captures 'b'
pattern = r"(a(b)c)"

# Using re.search() to find the pattern in the string 'abc'
match = re.search(pattern, "abc")

# Checking if a match is found
if match:
    # Printing the entire match (group 0)
    print("Entire match:", match.group(0))  # Output: abc
    
    # Printing the outer group (group 1)
    print("Outer group:", match.group(1))   # Output: abc
    
    # Printing the nested group (group 2)
    print("Nested group:", match.group(2))  # Output: b
