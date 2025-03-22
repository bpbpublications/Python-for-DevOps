# Script: 024_system_compliance_checks.py

import subprocess

def check_password_policy():
    """
    Checks if the password policy complies with standards by verifying 'PASS_MAX_DAYS' in /etc/login.defs.
    """
    try:
        with open('/etc/login.defs') as file:
            for line in file:
                if 'PASS_MAX_DAYS' in line and not line.startswith('#'):
                    max_days = int(line.split()[1])
                    if max_days > 90:
                        print("Compliance check failed: Password max days exceeds 90.")
                    else:
                        print("Compliance check passed: Password max days within limit.")
    except FileNotFoundError:
        print("File not found: /etc/login.defs. Unable to check password policy.")
    except PermissionError:
        print("Permission denied. Run this script with elevated privileges.")
    except Exception as e:
        print(f"An error occurred while checking password policy: {e}")

def check_firewall_status():
    """
    Checks if the firewall is active using UFW.
    """
    try:
        result = subprocess.run(['sudo', 'ufw', 'status'], capture_output=True, text=True)
        if 'Status: active' in result.stdout:
            print("Compliance check passed: Firewall is active.")
        else:
            print("Compliance check failed: Firewall is not active.")
    except FileNotFoundError:
        print("UFW is not installed. Unable to check firewall status.")
    except PermissionError:
        print("Permission denied. Run this script with elevated privileges.")
    except Exception as e:
        print(f"An error occurred while checking firewall status: {e}")

if __name__ == "__main__":
    # Run compliance checks
    check_password_policy()
    check_firewall_status()
