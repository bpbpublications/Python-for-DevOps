# Script: 027_parse_date.py

# Importing the datetime module for date manipulation
import datetime

# Sample date string in 'YYYY-MM-DD' format
date_str = '2023-04-12'

# Converting the date string to a datetime object using strptime
# The format '%Y-%m-%d' specifies the expected format of the input string
date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')

# Extracting the year, month, and day from the datetime object
year, month, day = date_obj.year, date_obj.month, date_obj.day

# Printing the extracted year, month, and day
print(f"Year: {year}, Month: {month}, Day: {day}")
