# Script: 018_add_link_to_jira_issue.py

import os
from jira import JIRA

def connect_to_jira():
    """
    Connects to a Jira instance using credentials stored in environment variables.
    :return: An authenticated Jira connection object.
    """
    # Get Jira credentials from environment variables
    jira_server = os.getenv('JIRA_SERVER')
    jira_user = os.getenv('JIRA_USER')
    jira_pass = os.getenv('JIRA_PASS')
    
    # Connect to Jira instance
    jira = JIRA(server=jira_server, basic_auth=(jira_user, jira_pass))
    
    return jira

def add_link_to_issue(issue_key, artifact_url, link_title):
    """
    Adds a link to the Jira issue, typically to a deployment artifact or other resource.
    :param issue_key: The key of the issue (e.g., 'PROJECT-123').
    :param artifact_url: The URL of the artifact to link to.
    :param link_title: The title for the link (e.g., 'Deployment Artifact').
    """
    # Get the Jira connection
    jira = connect_to_jira()
    
    # Get the issue by key
    issue = jira.issue(issue_key)
    
    # Add the link to the issue
    jira.add_simple_link(issue.key, {'url': artifact_url, 'title': link_title})

# Usage: Add a link to a specific Jira issue
issue_key = 'PROJECT-123'  # Replace with the actual issue key
artifact_url = "https://your-deployment-artifact-url.com"  # Replace with the actual artifact URL
link_title = "Deployment Artifact"
add_link_to_issue(issue_key, artifact_url, link_title)

# Print confirmation message
print(f"Link to {link_title} added to issue {issue_key} successfully.")
