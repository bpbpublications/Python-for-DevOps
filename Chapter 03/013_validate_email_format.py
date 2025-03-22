# Script: 013_validate_email_format.py

# Importing the 're' module to work with regular expressions
import re

# Sample email string to validate
email = "example@test.com"

# Using re.match() to check if the email matches a basic email pattern
# The pattern '[^@]+@[^@]+\.[^@]+' matches a simple email structure
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    # If the email matches the pattern, print "Valid email"
    print("Valid email")
else:
    # If the email does not match the pattern, print "Invalid email"
    print("Invalid email")
