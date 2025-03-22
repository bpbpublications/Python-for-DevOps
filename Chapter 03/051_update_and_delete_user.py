# Script: 051_update_and_delete_user.py

# Importing the requests module to make HTTP requests
import requests

# Update a user with new information
updated_info = {'name': 'Jane Smith'}
response = requests.put('https://api.example.com/users/123', json=updated_info)

# Delete a user by sending a DELETE request
response = requests.delete('https://api.example.com/users/123')
