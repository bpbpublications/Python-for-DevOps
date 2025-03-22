# Script: 016_create_and_manage_jira_issue.py

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

def create_jira_issue():
    """
    Creates a new Jira issue in a specified project and assigns labels.
    :return: The created issue object.
    """
    # Get the Jira connection
    jira = connect_to_jira()
    
    # Create a new issue in the 'PROJECT' project
    new_issue = jira.create_issue(
        project='PROJECT',  # Replace with the actual project key
        summary='Test Failed: Add details here',
        description='Test failed during CI/CD pipeline execution.',
        issuetype={'name': 'Bug'}  # Specify issue type (e.g., Bug, Task)
    )
    
    # Assign issue to a user (replace 'assignee_username' with the actual username)
    new_issue.update(assignee={'name': 'assignee_username'})
    
    # Add labels to the issue
    labels = new_issue.fields.labels + ['CI/CD']
    new_issue.update(fields={'labels': labels})
    
    return new_issue

# Usage: Create a Jira issue and manage its properties
new_issue = create_jira_issue()

# Print the created issue key (for confirmation)
print(f"Issue {new_issue.key} created and updated successfully.")
