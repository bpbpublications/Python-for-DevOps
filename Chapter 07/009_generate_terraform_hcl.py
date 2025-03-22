# Script: 009_generate_terraform_hcl.py

import os

# Example instance configurations
instances = [
    {"name": "instance1", "type": "t2.micro"},
    {"name": "instance2", "type": "t2.small"}
]

# Prepare Terraform HCL configuration
hcl_lines = []
for instance in instances:
    hcl_lines.append(f'resource "aws_instance" "{instance["name"]}" {{')
    hcl_lines.append(f'  ami           = "{os.getenv("AMI_ID")}"')  # Retrieve AMI ID from environment
    hcl_lines.append(f'  instance_type = "{instance["type"]}"')
    hcl_lines.append("}")

# Write the HCL configuration to a Terraform file
try:
    with open("main.tf", "w") as f:
        f.write("\n".join(hcl_lines))
    print("Terraform HCL config file generated.")
except Exception as e:
    print(f"Error writing Terraform HCL file: {e}")
