# Script: 021_extract_ip_addresses.py

# Importing the 're' module to work with regular expressions
import re

# Sample log string containing IP addresses
log = "Access from 192.168.1.1 and 10.0.0.1"

# Using re.findall() to find all IP addresses in the log
# The pattern '\b\d{1,3}(\.\d{1,3}){3}\b' matches an IP address with four octets separated by dots
ips = re.findall(r"\b\d{1,3}(\.\d{1,3}){3}\b", log)

# Printing the list of IP addresses found in the log
print("IP Addresses:", ips)
