# Script: 036_read_csv_file.py

# Importing the csv module to work with CSV data
import csv

# Opening the 'data.csv' file in read mode and reading the content
with open('data.csv', mode='r') as file:
    # Creating a CSV reader object to parse the file
    csv_reader = csv.reader(file)
    
    # Iterating through each row in the CSV file
    for row in csv_reader:
        # Printing each row, where each row is a list of values
        print(row)
