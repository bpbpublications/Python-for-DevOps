# Script: 001_extract_key_value_pairs.py

# Importing the 're' module to work with regular expressions
import re

# Sample text containing key-value pairs
text = "Username: user1, Age: 25, Country: USA"

# Regular expression pattern to match key-value pairs
# \w+ matches the key (one or more word characters)
# \S+ matches the value (one or more non-whitespace characters)
pattern = r"(\w+): (\S+)"

# Using findall() to find all matches of the pattern in the text
matches = re.findall(pattern, text)

# Iterating through the matches and printing the key-value pairs
for match in matches:
    print(f"Key: {match[0]}, Value: {match[1]}")
