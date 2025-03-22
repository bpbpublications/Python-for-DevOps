# Script: 007_split_string_by_comma.py

# Importing the 're' module to work with regular expressions
import re

# Using re.split() to split the string 'one,two,three' by the comma (',') delimiter
split_list = re.split(',', 'one,two,three')

# Printing the resulting list after splitting the string
print(split_list)
