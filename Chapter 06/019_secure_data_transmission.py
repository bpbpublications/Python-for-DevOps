# Script: 019_secure_data_transmission.py

import requests

def transmit_data(api_endpoint, data):
    """
    Sends data securely over HTTPS using a POST request.
    :param api_endpoint: The HTTPS API endpoint.
    :param data: The data to transmit as a dictionary.
    """
    try:
        # Sending data securely over HTTPS
        response = requests.post(api_endpoint, json=data, verify=True)
        
        if response.status_code == 200:
            print("Data transmitted securely.")
        else:
            print(f"Error in data transmission. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error during transmission: {e}")

if __name__ == "__main__":
    # Example usage
    api_endpoint = "https://example.com/api"  # Replace with your HTTPS API endpoint
    data = {"key": "value"}  # Replace with your data payload
    
    transmit_data(api_endpoint, data)
