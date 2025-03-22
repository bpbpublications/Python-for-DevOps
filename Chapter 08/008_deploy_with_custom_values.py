# Script: 008_deploy_with_custom_values.py

import subprocess

def deploy_with_custom_values(chart_path, release_name, namespace, custom_values):
    """
    Deploys or upgrades a Helm release with custom values provided.

    Args:
        chart_path (str): Path to the Helm chart.
        release_name (str): Name of the Helm release.
        namespace (str): Kubernetes namespace for the release.
        custom_values (str): YAML-formatted string of custom values for the Helm chart.
    """
    values_file = "custom_values.yaml"

    # Write the custom values to a temporary file
    with open(values_file, 'w') as file:
        file.write(custom_values)

    # Run the Helm upgrade/install command with the custom values file
    subprocess.run([
        "helm", "upgrade", "--install", release_name, chart_path, "-f", values_file, "--namespace", namespace
    ], check=True)

    print(f"Helm release '{release_name}' deployed/updated in namespace '{namespace}' using chart '{chart_path}'.")

# Example logic to generate custom values (replace with your own logic)
def generate_custom_values_based_on_logic():
    """
    Generate custom values for the Helm chart based on logic.

    Returns:
        str: YAML-formatted custom values.
    """
    return """
    replicaCount: 3
    image:
      repository: myapp
      tag: latest
    service:
      type: ClusterIP
      port: 80
    """

# Deploy the Helm chart with the generated custom values
if __name__ == "__main__":
    custom_values = generate_custom_values_based_on_logic()
    deploy_with_custom_values("./charts/myapp", "myapp-release", "default", custom_values)
