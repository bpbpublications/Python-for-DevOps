# Script: 010_find_non_vowel_characters.py

# Importing the 're' module to work with regular expressions
import re

# Using re.findall() to find all characters in the string 'hello world' that are not vowels
# The pattern '[^aeiou]' matches any character that is not a lowercase vowel
match = re.findall(r'[^aeiou]', 'hello world')

# Printing the list of non-vowel characters found
print("Non-vowel characters:", match)  # Output: ['h', 'l', 'l', ' ', 'w', 'r', 'l', 'd']
