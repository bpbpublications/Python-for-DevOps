# Script: 035_inject_secrets.py

import os

def inject_secrets():
    secret = get_secret("MyDatabasePassword")
    os.environ["DATABASE_PASSWORD"] = secret
    print("Secrets injected successfully.")

if __name__ == "__main__":
    inject_secrets()
