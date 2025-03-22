# Script: 013_generate_conditional_workflow.py

import yaml

def generate_conditional_workflow(branch_name):
    """
    Generates a conditional CI/CD pipeline workflow for GitHub Actions based on the branch name.
    If the branch is 'main', a deploy job is added to the pipeline.
    :param branch_name: The name of the branch that triggers the workflow.
    :return: A YAML string representing the CI/CD pipeline with conditional deployment.
    """
    workflow = """
name: CI/CD Pipeline

on:
  push:
    branches:
      - {branch}

jobs:
  build:
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
      
      - name: Run tests
        run: pytest
    """
    
    if branch_name == 'main':
        # Add deploy job only for the 'main' branch
        workflow += """
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
      
      - name: Deploy to production
        run: python deploy.py production
        """
    
    return workflow.format(branch=branch_name)

# Usage: Generate the workflow YAML for a specific branch (e.g., 'main')
branch_name = 'main'
workflow_yaml = generate_conditional_workflow(branch_name)

# Print the final generated YAML workflow
print(workflow_yaml)
