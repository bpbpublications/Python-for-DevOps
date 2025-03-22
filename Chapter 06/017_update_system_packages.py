# Script: 017_update_system_packages.py

import subprocess

def run_command(command):
    """
    Executes a system command and returns the output.
    :param command: Command to execute as a string.
    :return: Command output as a string, or None if the command fails.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing '{command}': {e.stderr.strip()}")
        return None

def update_system_packages():
    """
    Updates and upgrades system packages using apt-get.
    """
    print("Updating system packages...")
    update_command = "sudo apt-get update"
    upgrade_command = "sudo apt-get upgrade -y"

    # Run update command
    update_output = run_command(update_command)
    if update_output:
        print(update_output)

    # Run upgrade command
    upgrade_output = run_command(upgrade_command)
    if upgrade_output:
        print(upgrade_output)

if __name__ == "__main__":
    update_system_packages()
