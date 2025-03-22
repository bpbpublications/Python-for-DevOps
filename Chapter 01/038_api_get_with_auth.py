import requests
import os

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/todos/1"

# Retrieve the API key from an environment variable
api_key = os.getenv('API_KEY')  # Set 'API_KEY' in your environment variables

if not api_key:
    print("Error: API key not found. Please set it in your environment variables.")
else:
    # Set up the headers with the API key
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Make a GET request to the API with authorization headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON content
        data = response.json()
        # Print the retrieved data
        print(data)
    else:
        # Print an error message if the request failed
        print(f"Failed to retrieve data. Status code: {response.status_code}")
