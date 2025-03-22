import subprocess
import platform

def ping_servers(servers):
    """
    Pings a list of servers and reports their status.
    """
    # Determine the ping command based on the operating system
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    for server in servers:
        try:
            # Execute the ping command
            response = subprocess.call(["ping", param, "1", server], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if response == 0:
                print(f"{server} is up!")
            else:
                print(f"{server} is down!")
        except Exception as e:
            print(f"Error pinging {server}: {e}")

# List of servers to ping
servers = ["8.8.8.8", "8.8.4.4", "192.168.1.1"]

# Ping the servers
ping_servers(servers)
