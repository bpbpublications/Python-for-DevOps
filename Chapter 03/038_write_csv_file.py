# Script: 038_write_csv_file.py

# Importing the csv module to work with CSV data
import csv

# Opening the 'output.csv' file in write mode
# 'newline=""' ensures that no extra blank lines are added between rows on Windows
with open('output.csv', mode='w', newline='') as file:
    # Creating a CSV writer object to write data to the file
    csv_writer = csv.writer(file)
    
    # Writing the header row to the CSV file
    csv_writer.writerow(['Name', 'Age'])
    
    # Writing data rows to the CSV file
    csv_writer.writerow(['Alice', 24])
    csv_writer.writerow(['Bob', 22])
