# Script: 011_report_incident_request.py

import requests

# Incident data to be reported
data = {
    "type": "service_outage",  # Type of the incident
    "description": "Service XYZ is down",  # Description of the incident
    "reporter": "John Doe"  # Reporter of the incident
}

# Send a POST request to report the incident
response = requests.post("http://localhost:5000/report-incident", json=data)

# Print the response from the server
print(response.json())
