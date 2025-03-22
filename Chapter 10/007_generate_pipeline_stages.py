# Script: 007_generate_pipeline_stages.py

import yaml

def generate_build_stage():
    """
    Generates the build stage for the pipeline.
    :return: A YAML string representing the build stage.
    """
    build_stage = """
build:
  stage: build
  script:
    - echo "Building application..."
    """
    return build_stage

def generate_test_stage():
    """
    Generates the test stage for the pipeline.
    :return: A YAML string representing the test stage.
    """
    test_stage = """
test:
  stage: test
  script:
    - echo "Running tests..."
    """
    return test_stage

# Usage: Generate the full pipeline YAML
pipeline_yaml = f"""
stages:
  - build
  - test

{generate_build_stage()}
{generate_test_stage()}
"""

# Print the final generated YAML pipeline
print(pipeline_yaml)
