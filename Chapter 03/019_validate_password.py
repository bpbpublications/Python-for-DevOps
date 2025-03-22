# Script: 019_validate_password.py

# Importing the 're' module to work with regular expressions
import re

# Sample password string to validate
password = "Pass1234"

# Using re.match() to check if the password contains at least one digit and is at least 8 characters long
# The pattern '(?=.*\d).{8,}' checks for:
# - '(?=.*\d)' ensures at least one digit is present
# - '.{8,}' ensures the password is at least 8 characters long
if re.match(r"(?=.*\d).{8,}", password):
    # If the password matches the pattern, print "Valid password"
    print("Valid password")
else:
    # If the password does not match the pattern, print "Invalid password"
    print("Invalid password")
