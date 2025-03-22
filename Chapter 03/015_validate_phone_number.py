# Script: 015_validate_phone_number.py

# Importing the 're' module to work with regular expressions
import re

# Sample phone number string to validate
phone = "123-456-7890"

# Using re.match() to check if the phone number matches the format 'xxx-xxx-xxxx'
# The pattern '\b\d{3}-\d{3}-\d{4}\b' matches a phone number with 3 digits, followed by a hyphen, 3 digits, another hyphen, and 4 digits
if re.match(r"\b\d{3}-\d{3}-\d{4}\b", phone):
    # If the phone number matches the pattern, print "Valid phone number"
    print("Valid phone number")
else:
    # If the phone number does not match the pattern, print "Invalid phone number"
    print("Invalid phone number")
