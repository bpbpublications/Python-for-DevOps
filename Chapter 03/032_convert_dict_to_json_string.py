# Script: 032_convert_dict_to_json_string.py

# Importing the json module to work with JSON data
import json

# Dictionary to be converted to a JSON string
data = {
    'id': 1,
    'title': 'Hello World',
    'body': 'This is a post.'
}

# Converting the dictionary to a JSON string using json.dumps()
json_string = json.dumps(data)

# Printing the resulting JSON string
print(json_string)  # '{"id": 1, "title": "Hello World", "body": "This is a post."}'
