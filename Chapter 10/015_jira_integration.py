# Script: 015_jira_integration.py

import os
from jira import JIRA

def connect_to_jira():
    """
    Connects to a Jira instance using credentials stored in environment variables.
    :return: An authenticated Jira connection object.
    """
    # Get credentials from environment variables
    jira_server = os.getenv('JIRA_SERVER')
    jira_user = os.getenv('JIRA_USER')
    jira_pass = os.getenv('JIRA_PASS')
    
    # Connect to Jira instance
    jira = JIRA(server=jira_server, basic_auth=(jira_user, jira_pass))
    
    return jira

def transition_issue_to_deployed(issue_key):
    """
    Transitions a Jira issue to the 'Deployed' status.
    :param issue_key: The key of the issue to be transitioned (e.g., 'PROJECT-123').
    """
    # Get the Jira connection
    jira = connect_to_jira()
    
    # Get the issue by key
    issue = jira.issue(issue_key)
    
    # Transition the issue to 'Deployed' status
    jira.transition_issue(issue, 'Deployed')
    
# Usage: Transition an issue to 'Deployed' status
issue_key = 'PROJECT-123'  # Replace with the actual issue key
transition_issue_to_deployed(issue_key)
