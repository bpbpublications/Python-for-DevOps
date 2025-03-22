# Script: 004_manage_iptables_rules.py

import subprocess

def run_command(command):
    """
    Executes a shell command and returns the output.
    Handles exceptions and returns stderr if an error occurs.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

def list_rules(table='filter'):
    """
    Lists all rules in the specified iptables table.
    """
    print(f"Listing {table} table rules...")
    return run_command(f"sudo iptables -t {table} -L -v")

def add_rule(rule, table='filter'):
    """
    Adds a rule to the specified iptables table.
    """
    print(f"Adding rule to {table} table: {rule}")
    return run_command(f"sudo iptables -t {table} {rule}")

def delete_rule(rule, table='filter'):
    """
    Deletes a rule from the specified iptables table.
    """
    print(f"Deleting rule from {table} table: {rule}")
    return run_command(f"sudo iptables -t {table} {rule}")

if __name__ == "__main__":
    try:
        # List all rules in the default "filter" table
        print(list_rules())

        # Example to add a rule (Be cautious with the rule you add)
        rule_to_add = '-A INPUT -p tcp --dport 22 -j ACCEPT'
        print(add_rule(rule_to_add))

        # Example to delete a rule (Be cautious with the rule you delete)
        rule_to_delete = '-D INPUT -p tcp --dport 22 -j ACCEPT'
        print(delete_rule(rule_to_delete))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
