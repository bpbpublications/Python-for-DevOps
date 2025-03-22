# Script: 008_file_handling_with_finally.py

try:
    # Open the file in read mode
    file = open('data.txt', 'r')
    data = file.read()
finally:
    # Ensure the file is closed regardless of success or failure
    file.close()

# Process or print the data (optional)
print(data)
