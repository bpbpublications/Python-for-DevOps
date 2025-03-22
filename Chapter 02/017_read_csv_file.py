# Script: Read CSV File
# Purpose: Demonstrates how to read a CSV file and print the first column using the `csv` module.

import csv

# Define the path to the CSV file
csv_file = 'file.csv'  # Replace with the path to your CSV file

try:
    # Open the CSV file
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)

        # Iterate over each row and print the first column
        print("First column values:")
        for row in reader:
            if row:  # Ensure the row is not empty
                print(row[0])  # Prints the first column
except FileNotFoundError:
    print(f"Error: The file '{csv_file}' does not exist.")
except IndexError:
    print("Error: The row does not contain enough columns.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
