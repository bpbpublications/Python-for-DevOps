# Script: 041_create_grafana_dashboard.py

import requests

def create_grafana_dashboard(api_url, api_key, dashboard_config):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(f"{api_url}/api/dashboards/db", headers=headers, json=dashboard_config)
        if response.status_code == 200:
            print("Grafana dashboard created successfully.")
        else:
            print(f"Error creating dashboard: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    grafana_api_url = "http://localhost:3000"
    grafana_api_key = "your-api-key"
    dashboard_config = {
        "dashboard": {
            "id": None,
            "uid": None,
            "title": "MyAppDashboard",
            "panels": [],
        },
        "overwrite": True
    }
    create_grafana_dashboard(grafana_api_url, grafana_api_key, dashboard_config)
