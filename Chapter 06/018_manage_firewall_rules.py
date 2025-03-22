# Script: 018_manage_firewall_rules.py

import subprocess

def run_command(command):
    """
    Executes a shell command and prints the output or error.
    :param command: Command to execute as a list of strings.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {' '.join(command)}")
        print(f"Details: {e.stderr.strip()}")

def add_firewall_rule(rule):
    """
    Adds a firewall rule using iptables.
    :param rule: The iptables rule to add as a string.
    """
    try:
        command = f"sudo iptables {rule}"
        run_command(command)
        print(f"Firewall rule added: {rule}")
    except Exception as e:
        print(f"Error adding firewall rule: {e}")

def save_firewall_rules():
    """
    Saves the current iptables rules.
    """
    try:
        command = "sudo iptables-save"
        run_command(command)
        print("Firewall rules saved successfully.")
    except Exception as e:
        print(f"Error saving firewall rules: {e}")

if __name__ == "__main__":
    # Example usage: Adding a rule to accept HTTP traffic
    rule_to_add = "-A INPUT -p tcp --dport 80 -j ACCEPT"  # Accept HTTP traffic
    add_firewall_rule(rule_to_add)
    
    # Save the rules
    save_firewall_rules()
