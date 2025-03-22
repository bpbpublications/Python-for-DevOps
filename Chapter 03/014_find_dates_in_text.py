# Script: 014_find_dates_in_text.py

# Importing the 're' module to work with regular expressions
import re

# Sample text containing a date
text = "The event is on 12/05/2023."

# Using re.findall() to find all dates in the format 'dd/mm/yyyy'
# The pattern '\b\d{2}/\d{2}/\d{4}\b' matches a date with two digits for day, month, and four digits for year
dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)

# Printing the list of dates found in the text
print("Dates found:", dates)
