# Script: 025_check_and_update_package.py

import subprocess
import pkg_resources

def check_and_update_package(package_name):
    """
    Checks the installed version of a package and updates it if a newer version is available.
    :param package_name: Name of the package to check and update.
    """
    try:
        # Get the current version of the package
        current_version = pkg_resources.get_distribution(package_name).version

        # Get the latest available version of the package from PyPI
        latest_version = subprocess.getoutput(f"pip search {package_name} | grep -E '^{package_name}'").split()[-1].strip("()")

        if current_version != latest_version:
            print(f"Updating {package_name} from {current_version} to {latest_version}")
            subprocess.run(f"pip install --upgrade {package_name}", shell=True, check=True)
        else:
            print(f"{package_name} is up-to-date. Current version: {current_version}")

    except pkg_resources.DistributionNotFound:
        print(f"Package '{package_name}' is not installed.")
        print(f"Installing {package_name}...")
        subprocess.run(f"pip install {package_name}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error checking or updating package '{package_name}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    check_and_update_package('requests')  # Replace 'requests' with the package you want to check and update
