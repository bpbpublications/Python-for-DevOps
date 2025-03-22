# Script: 022_create_grafana_dashboard.py

import requests

# Grafana API endpoint
url = 'http://localhost:3000/api/dashboards/db'

# Dashboard configuration
dashboard_config = {
    "dashboard": {
        "id": None,  # Set to None for a new dashboard
        "title": "Sample Dashboard",  # Title of the dashboard
        "panels": [],  # Define your panels here
        "timezone": "browser",  # Use the browser's timezone
        "schemaVersion": 16,  # Grafana schema version
        "version": 0  # Initial version of the dashboard
    },
    "overwrite": False  # Set to True to overwrite an existing dashboard with the same title
}

# Send POST request to create the dashboard
headers = {
    "Authorization": "Bearer <YOUR_API_KEY>",  # Replace <YOUR_API_KEY> with your Grafana API key
    "Content-Type": "application/json"
}
response = requests.post(url, json=dashboard_config, headers=headers)

# Print response
print(response.status_code)  # Print the HTTP status code
print(response.json())  # Print the response JSON
