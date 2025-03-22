# Script: Download File from URL
# Purpose: Demonstrates how to download a file from a URL using the `requests` module.

import requests

# Define the URL and output file name
url = 'http://example.com/file'  # Replace with the URL of the file to download
output_file = 'file'  # Replace with the desired local file name

try:
    # Send a GET request to the URL
    print(f"Downloading file from: {url}")
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError if the response contains an HTTP error status code

    # Write the content to a local file in binary mode
    with open(output_file, 'wb') as f:
        f.write(response.content)
    print(f"File downloaded successfully and saved as: {output_file}")
except requests.exceptions.RequestException as e:
    # Handle any request-related errors
    print(f"Error: Failed to download the file. Details: {e}")
except Exception as e:
    # Handle any unexpected errors
    print(f"An unexpected error occurred: {e}")
