# Script: 031_write_json_to_file.py

# Importing the json module to work with JSON data
import json

# Dictionary to be converted to JSON and saved to a file
data = {
     'name': 'Jane',
     'age': 25,
     'city': 'Los Angeles'
}

# Opening 'output.json' file in write mode and dumping the data as JSON
with open('output.json', 'w') as file:
    # Writing the dictionary data to the file as JSON
    json.dump(data, file)
