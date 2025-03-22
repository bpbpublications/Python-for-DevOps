# Script: 017_add_comment_to_jira_issue.py

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

def add_comment_to_issue(issue_key, comment_text):
    """
    Adds a comment to a specified Jira issue.
    :param issue_key: The key of the issue (e.g., 'PROJECT-123').
    :param comment_text: The text of the comment to be added to the issue.
    """
    # Get the Jira connection
    jira = connect_to_jira()
    
    # Get the issue by key
    issue = jira.issue(issue_key)
    
    # Add the comment to the issue
    jira.add_comment(issue, comment_text)

# Usage: Add a comment to a specific Jira issue
issue_key = 'PROJECT-123'  # Replace with the actual issue key
comment_text = "CI/CD Pipeline: Success"
add_comment_to_issue(issue_key, comment_text)

# Print confirmation message
print(f"Comment added to issue {issue_key} successfully.")
