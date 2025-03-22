# Script: 001_fetch_device_status.py

import os
import requests

# API endpoint for network device status
url = "https://network-device/api/status"

# API authentication credentials
auth_credentials = (os.getenv('API_USERNAME'), os.getenv('API_PASSWORD'))

try:
    # Send GET request to the API
    response = requests.get(url, auth=auth_credentials, timeout=10)  # Added a timeout for safety
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()
        # Print the device status
        print("Device Status:", data.get('status', 'Unknown'))  # Added default value for safety
    else:
        # Print an error message with the status code
        print(f"Failed to retrieve data: {response.status_code}")
except requests.exceptions.Timeout:
    # Handle request timeout
    print("Request timed out")
except requests.exceptions.RequestException as e:
    # Handle other request-related exceptions
    print(f"Request error: {e}")
except Exception as e:
    # Handle general exceptions
    print(f"An unexpected error occurred: {e}")
