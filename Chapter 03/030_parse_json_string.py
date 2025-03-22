# Script: 030_parse_json_string.py

# Importing the json module to work with JSON data
import json

# JSON string to be parsed
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parsing the JSON string into a Python object (dict)
parsed_data = json.loads(json_string)

# Printing the parsed data (Python dictionary)
print(parsed_data)  # {'name': 'John', 'age': 30, 'city': 'New York'}
