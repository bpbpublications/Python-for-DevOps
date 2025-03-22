# Script: 018_watch_config_changes_etcd.py

import etcd3

# Function to watch for configuration changes in etcd for a specific service
def watch_config_changes(service_name):
    etcd = etcd3.client()  # Create an etcd client instance

    # Define the callback function to handle configuration changes
    def callback(event):
        print(f"Configuration change detected: {event.key}")  # Print the key of the changed configuration
        # Logic to apply the new configuration can be added here

    # Watch for changes under the service's config key prefix
    watch_id = etcd.add_watch_prefix_callback(f"config/{service_name}/", callback)
    return watch_id

# Watch for configuration changes in "my_microservice"
watch_id = watch_config_changes("my_microservice")
