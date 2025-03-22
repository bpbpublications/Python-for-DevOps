# Script: 006_compile_pattern_and_match.py

# Importing the 're' module to work with regular expressions
import re

# Compiling the regular expression pattern 'py' into a pattern object
pattern = re.compile('py')

# Using the compiled pattern to match the start of the string 'python'
match = pattern.match('python')

# Checking if a match is found
if match:
    # If a match is found, print the matched string
    print("Match found:", match.group())
