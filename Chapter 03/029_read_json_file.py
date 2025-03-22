# Script: 029_read_json_file.py

# Importing the json module to work with JSON data
import json

# Assuming 'data.json' contains JSON data
# Opening the 'data.json' file in read mode and loading the content
with open('data.json', 'r') as file:
    # Loading the JSON data from the file into a Python object (dict or list)
    data = json.load(file)
    
    # Printing the loaded data (Python object)
    print(data)  # Python object (dict or list)
