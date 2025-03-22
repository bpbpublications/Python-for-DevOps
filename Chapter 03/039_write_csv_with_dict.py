# Script: 039_write_csv_with_dict.py

# Importing the csv module to work with CSV data
import csv

# Opening the 'output.csv' file in write mode
# 'newline=""' ensures that no extra blank lines are added between rows on Windows
with open('output.csv', mode='w', newline='') as file:
    # Defining the fieldnames (column names) for the CSV file
    fieldnames = ['Name', 'Age']
    
    # Creating a CSV DictWriter object to write dictionaries to the file
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Writing the header row to the CSV file
    csv_writer.writeheader()
    
    # Writing data rows as dictionaries to the CSV file
    csv_writer.writerow({'Name': 'Alice', 'Age': 24})
    csv_writer.writerow({'Name': 'Bob', 'Age': 22})
