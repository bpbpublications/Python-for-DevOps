# Script: 010_generate_github_actions_pipeline.py

import yaml

def generate_build_stage():
    """
    Generates the build stage for a GitHub Actions CI pipeline.
    :return: A YAML string representing the build stage.
    """
    build_stage = """
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
    """
    return build_stage

def generate_test_stage():
    """
    Generates the test stage for a GitHub Actions CI pipeline.
    :return: A YAML string representing the test stage.
    """
    test_stage = """
test:
  runs-on: ubuntu-latest
  
  steps:
    - name: Checkout code
      uses: actions/checkout@v2
      
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Run tests
      run: pytest
    """
    return test_stage

# Usage: Generate the full GitHub Actions CI/CD pipeline YAML
pipeline_yaml = f"""
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  {generate_build_stage()}
  {generate_test_stage()}
"""

# Print the final generated YAML pipeline for GitHub Actions
print(pipeline_yaml)
