# Script: 014_custom_action_workflow.py

import yaml

def custom_action_workflow():
    """
    Generates a CI/CD pipeline workflow that includes a custom action in GitHub Actions.
    This example assumes you are using a custom action (e.g., `my-custom-action@v1`) for a specific task.
    :return: A YAML string representing the CI/CD workflow with the custom action.
    """
    workflow = """
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  custom_action:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Run custom action
        uses: my-custom-action@v1
    """
    return workflow

# Usage: Generate the workflow YAML with a custom action
workflow_yaml = custom_action_workflow()

# Print the final generated YAML workflow
print(workflow_yaml)
