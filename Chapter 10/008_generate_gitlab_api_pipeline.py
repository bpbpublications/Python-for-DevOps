# Script: 008_generate_gitlab_api_pipeline.py

import yaml

def generate_gitlab_api_pipeline():
    """
    Generates a GitLab API pipeline task to trigger a downstream pipeline.
    :return: A YAML string representing the GitLab API task for triggering a downstream pipeline.
    """
    gitlab_api_tasks = """
trigger_downstream_pipeline:
  stage: deploy
  script:
    - curl -X POST -F token=$CI_JOB_TOKEN -F ref=master https://gitlab.example.com/api/v4/projects/123/trigger/pipeline
    """
    return gitlab_api_tasks

# Usage: Generate the full pipeline YAML
pipeline_yaml = f"""
stages:
  - deploy

{generate_gitlab_api_pipeline()}
"""

# Print the final generated YAML pipeline
print(pipeline_yaml)
