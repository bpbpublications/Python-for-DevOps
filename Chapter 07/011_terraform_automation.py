# Script: 011_terraform_automation.py

import subprocess

def run_terraform_command(command):
    """
    Run a Terraform command and print the result.

    Args:
        command (str): The Terraform command to execute (e.g., 'init', 'plan', 'apply').

    Returns:
        int: The return code of the command execution.
    """
    try:
        # Execute the Terraform command
        result = subprocess.run(["terraform", command], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Successfully executed: terraform {command}")
        else:
            print(f"Error in executing: terraform {command}")
            print(result.stderr)
        
        return result.returncode
    except Exception as e:
        print(f"An error occurred while running 'terraform {command}': {e}")
        return 1

# Automate Terraform Init, Plan, and Apply
if __name__ == "__main__":
    if run_terraform_command("init") == 0 and run_terraform_command("plan") == 0:
        run_terraform_command("apply")
