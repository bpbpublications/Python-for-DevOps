# Script: 017_extract_domain_from_url.py

# Importing the 're' module to work with regular expressions
import re

# Sample URL to extract the domain from
url = "https://www.example.com/page"

# Using re.search() to extract the domain from the URL
# The pattern 'https?://([\w.-]+)/' matches the protocol (http or https), followed by the domain
domain = re.search(r"https?://([\w.-]+)/", url).group(1)

# Printing the extracted domain
print("Domain:", domain)
