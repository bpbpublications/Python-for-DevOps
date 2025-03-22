# Script: 006_generate_dynamic_pipeline.py

import yaml

def generate_dynamic_pipeline(branch_name):
    """
    Generates a dynamic pipeline configuration based on the branch name.
    :param branch_name: The branch name (e.g., 'master', 'develop').
    :return: A YAML string representing the pipeline configuration.
    """
    
    if branch_name == 'master':
        # Pipeline configuration for the 'master' branch (production)
        pipeline_config = """
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - echo "Building application..."

test:
  stage: test
  script:
    - echo "Running tests..."

deploy:
  stage: deploy
  script:
    - echo "Deploying to production..."
        """
    else:
        # Pipeline configuration for other branches (e.g., 'develop')
        pipeline_config = """
stages:
  - build
  - test

build:
  stage: build
  script:
    - echo "Building application..."

test:
  stage: test
  script:
    - echo "Running tests..."
        """
    
    return pipeline_config

# Usage
branch_name = 'master'  # Can be 'master' or any other branch name
pipeline_yaml = generate_dynamic_pipeline(branch_name)

# Convert the generated YAML string into a Python dictionary (optional)
pipeline_dict = yaml.safe_load(pipeline_yaml)

# Print the YAML pipeline for visualization or further use
print(pipeline_yaml)
