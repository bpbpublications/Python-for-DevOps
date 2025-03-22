# Script: Read JSON File
# Purpose: Demonstrates how to read a JSON file and access a specific key using the `json` module.

import json

# Define the path to the JSON file
json_file = 'file.json'  # Replace with the path to your JSON file

try:
    # Open the JSON file and load its content
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Access and print the value associated with a specific key
    # Replace 'key' with the actual key you want to access
    print("Value for 'key':", data['key'])
except FileNotFoundError:
    print(f"Error: The file '{json_file}' does not exist.")
except KeyError:
    print("Error: The specified key 'key' was not found in the JSON file.")
except json.JSONDecodeError:
    print(f"Error: The file '{json_file}' does not contain valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
