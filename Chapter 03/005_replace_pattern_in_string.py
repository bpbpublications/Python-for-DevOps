# Script: 005_replace_pattern_in_string.py

# Importing the 're' module to work with regular expressions
import re

# Using re.sub() to replace occurrences of 'python' with 'Perl' in the string 'I love python'
replaced_string = re.sub('python', 'Perl', 'I love python')

# Printing the string after the replacement
print(replaced_string)
