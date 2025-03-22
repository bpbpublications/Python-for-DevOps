# Script: 006_manage_helm_charts.py

import subprocess

def install_helm_chart(release_name, chart_name):
    """
    Installs a Helm chart with the given release name.

    Args:
        release_name (str): The name of the Helm release.
        chart_name (str): The name of the Helm chart to install.
    """
    subprocess.run(["helm", "install", release_name, chart_name], check=True)
    print(f"Helm chart '{chart_name}' installed with release name '{release_name}'.")

def update_helm_chart(release_name, chart_name):
    """
    Updates a Helm release with the given release name and chart.

    Args:
        release_name (str): The name of the Helm release to update.
        chart_name (str): The name of the Helm chart to upgrade.
    """
    subprocess.run(["helm", "upgrade", release_name, chart_name], check=True)
    print(f"Helm release '{release_name}' upgraded with chart '{chart_name}'.")

def delete_helm_release(release_name):
    """
    Deletes a Helm release with the given release name.

    Args:
        release_name (str): The name of the Helm release to delete.
    """
    subprocess.run(["helm", "uninstall", release_name], check=True)
    print(f"Helm release '{release_name}' uninstalled.")

# Example usage
if __name__ == "__main__":
    # Example operations (uncomment and modify as needed)
    # install_helm_chart("my-release", "nginx")
    # update_helm_chart("my-release", "nginx")
    # delete_helm_release("my-release")
    pass
