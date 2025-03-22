# Script: 052_handle_api_response.py

# Importing the requests module to make HTTP requests
import requests

# Sending a GET request to the API to retrieve user data
response = requests.get('https://api.example.com/users/123')

# Checking if the response status code indicates success (200 OK)
if response.status_code == 200:
    # Parsing the JSON response into a Python dictionary
    user_data = response.json()
else:
    # Printing an error message with the status code if the request fails
    print(f"Error: {response.status_code}")
