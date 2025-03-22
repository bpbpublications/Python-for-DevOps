# Script: 007_manage_helm_releases_with_pyhelm.py

from pyhelm.chartbuilder import ChartBuilder
from pyhelm.tiller import Tiller

# Initialize Tiller with the TILLER_HOST environment variable or specific host
tiller = Tiller('TILLER_HOST')  # Replace 'TILLER_HOST' with the actual Tiller host

# Define a Helm chart from a repository
chart = ChartBuilder({
    "name": "my-chart",
    "source": {
        "type": "repo",  # Source type ('repo' for chart repository)
        "location": "CHART_REPO_URL"  # Replace with the actual chart repository URL
    }
})

# Install a Helm chart
tiller.install_release(
    chart.get_helm_chart(),  # Retrieve the Helm chart object
    dry_run=False,  # Set to True for a dry-run installation
    namespace='default'  # Namespace where the release will be installed
)
print("Helm chart 'my-chart' installed in the 'default' namespace.")

# List all Helm releases
releases = tiller.list_releases()
print("Current Helm releases:")
for release in releases:
    print(f"Name: {release.name}, Namespace: {release.namespace}, Status: {release.info.status}")
