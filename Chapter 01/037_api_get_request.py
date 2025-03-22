import requests

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/todos/1"

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON content
    data = response.json()
    # Print the retrieved data
    print(data)
else:
    # Print an error message if the request failed
    print(f"Failed to retrieve data. Status code: {response.status_code}")
