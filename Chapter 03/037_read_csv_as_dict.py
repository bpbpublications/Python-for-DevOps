# Script: 037_read_csv_as_dict.py

# Importing the csv module to work with CSV data
import csv

# Opening the 'data.csv' file in read mode and reading the content
with open('data.csv', mode='r') as file:
    # Creating a CSV DictReader object to parse the file into dictionaries
    csv_reader = csv.DictReader(file)
    
    # Iterating through each row in the CSV file
    for row in csv_reader:
        # Printing each row, where each row is an OrderedDict (column names as keys)
        print(row)
