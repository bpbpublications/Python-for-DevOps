# Script: 015_check_security_headers.py

import requests

# Function to check for required security headers in the HTTP response
def check_security_headers(url):
    headers = requests.get(url).headers  # Fetch the headers from the URL
    required = ['Strict-Transport-Security', 'Content-Security-Policy']  # List of required headers
    missing = [h for h in required if h not in headers]  # Identify missing headers
    return not missing, missing  # Return True if all headers are present, along with any missing headers

# URL to check for security headers
url = "https://example.com"

# Check for compliance with the required headers
compliant, missing = check_security_headers(url)

# Output the result, including any missing headers
print(f"Missing headers: {missing}" if not compliant else "All security headers are present.")
