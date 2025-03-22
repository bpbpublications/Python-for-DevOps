# Script: 003_fetch_network_data.py

import requests

# URL of the network service
url = "https://network-device/api/data"

try:
    # Send GET request to the URL with SSL verification enabled (default behavior)
    response = requests.get(url, verify=True, timeout=10)  # Added timeout for safety
    if response.status_code == 200:
        # Print the retrieved data
        print("Successfully retrieved data:")
        print(response.json())
    else:
        # Handle non-success status codes
        print(f"Failed to retrieve data. Status code: {response.status_code}")
except requests.exceptions.SSLError as e:
    # Handle SSL errors
    print("SSL Error:", e)
except requests.exceptions.RequestException as e:
    # Handle other request-related exceptions
    print("Request Error:", e)
except Exception as e:
    # Handle general exceptions
    print("Error:", e)
