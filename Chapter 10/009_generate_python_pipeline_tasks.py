# Script: 009_generate_python_pipeline_tasks.py

import yaml

def generate_python_pipeline_tasks():
    """
    Generates a Python-specific pipeline with tasks for installing dependencies, 
    linting code, and running tests.
    :return: A YAML string representing the pipeline tasks for Python.
    """
    python_tasks = """
install_dependencies:
  stage: build
  script:
    - pip install -r requirements.txt

lint_code:
  stage: test
  script:
    - pylint *.py

run_tests:
  stage: test
  script:
    - pytest
    """
    return python_tasks

# Usage: Generate the full pipeline YAML
pipeline_yaml = f"""
stages:
  - build
  - test

{generate_python_pipeline_tasks()}
"""

# Print the final generated YAML pipeline
print(pipeline_yaml)
