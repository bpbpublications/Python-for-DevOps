# Script: 049_api_request_with_params.py

# Importing the requests module to make HTTP requests
import requests

# Defining the query parameters for the API request
params = {'page': 2, 'limit': 20}

# Sending a GET request to the API with the specified URL and parameters
response = requests.get('https://api.example.com/users/123', params=params)

# Parsing the response JSON content into a Python dictionary
user_data = response.json()
