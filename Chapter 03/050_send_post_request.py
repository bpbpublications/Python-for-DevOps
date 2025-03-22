# Script: 050_send_post_request.py

# Importing the requests module to make HTTP requests
import requests

# Defining the payload data to send in the POST request
user_payload = {'name': 'Jane Doe', 'email': 'jane@example.com'}

# Sending a POST request to the API with the specified URL and payload
response = requests.post('https://api.example.com/users', json=user_payload)
