# Script: 011_generate_parameterized_workflow.py

import yaml

def generate_parameterized_workflow(environment):
    """
    Generates a parameterized CI/CD workflow for GitHub Actions based on the given environment.
    :param environment: The environment to deploy to (e.g., 'production', 'staging').
    :return: A YAML string representing the parameterized workflow.
    """
    workflow = """
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
      
      - name: Deploy to {env}
        run: python deploy.py {env}
    """.format(env=environment)
    
    return workflow

# Usage: Generate the full workflow YAML with a parameterized environment
environment = 'production'  # Can be 'production', 'staging', etc.
workflow_yaml = generate_parameterized_workflow(environment)

# Print the final generated YAML workflow
print(workflow_yaml)
