# Script: 012_deploy_to_aws.py

import yaml

def deploy_to_aws():
    """
    Generates a CI/CD pipeline workflow for deployment to AWS, which is used by GitHub Actions.
    :return: A YAML string representing the CI/CD pipeline for AWS deployment.
    """
    deployment_script = """
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Deploy to AWS
        run: python deploy_to_aws.py
    """
    
    return deployment_script

# Usage: Generate the deployment pipeline YAML
workflow_yaml = deploy_to_aws()

# Print the final generated YAML for the GitHub Actions pipeline
print(workflow_yaml)
