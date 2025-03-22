# Script: 017_fetch_config_from_consul.py

import requests

# Function to fetch configuration from Consul for a specific service
def fetch_config_from_consul(service_name):
    consul_url = f"http://consul-server:8500/v1/kv/config/{service_name}"  # Consul API endpoint for the service config
    response = requests.get(consul_url)  # Send GET request to Consul
    if response.status_code == 200:
        config = response.json()[0]['Value']  # Extract the configuration value from the response
        return config
    else:
        raise Exception("Failed to fetch configuration")  # Raise an exception if the request fails

# Fetch configuration for a specific service
service_config = fetch_config_from_consul("my_microservice")

# Process and apply the service_config as needed
