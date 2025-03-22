# Script: 005_scrape_network_status.py

import requests
from bs4 import BeautifulSoup

# URL of the network device's status page
url = "http://network-device/status"

try:
    # Send GET request to the URL
    response = requests.get(url, timeout=10)  # Added timeout for safety

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the status div
        status = soup.find('div', id='status')
        
        # Print the network device status
        print(f"Network Device Status: {status.get_text().strip()}" if status else "Status not found on the page.")
    else:
        # Handle non-success status codes
        print(f"Failed to retrieve page, status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    # Handle request-related exceptions
    print(f"Request error: {e}")
except Exception as e:
    # Handle general exceptions
    print(f"Error: {e}")
