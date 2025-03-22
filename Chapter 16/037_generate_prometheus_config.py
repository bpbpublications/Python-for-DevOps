# Script: 037_generate_prometheus_config.py

import json

def generate_prometheus_config(job_name, target):
    config = {
        "global": {"scrape_interval": "15s"},
        "scrape_configs": [
            {
                "job_name": job_name,
                "static_configs": [{"targets": [target]}]
            }
        ]
    }

    with open("prometheus.yml", "w") as file:
        json.dump(config, file, indent=2)
    print("Prometheus configuration generated successfully.")

if __name__ == "__main__":
    generate_prometheus_config("my-app", "localhost:8000")
