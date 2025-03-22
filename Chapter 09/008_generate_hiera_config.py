# Script: 008_generate_hiera_config.py

import yaml

# Define the configuration data
data = {
    'application_port': 8080,
    'service_enabled': True
}

# Write the data to a Hiera YAML configuration file
with open('/etc/puppetlabs/code/environments/production/hieradata/dynamic_config.yaml', 'w') as file:
    yaml.dump(data, file)
