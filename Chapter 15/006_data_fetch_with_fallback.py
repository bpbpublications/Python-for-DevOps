# Script: 006_data_fetch_with_fallback.py

# Placeholder exception and data fetch functions
class DataSourceUnavailable(Exception):
    """
    Custom exception to simulate the unavailability of a primary data source.
    """
    pass

def fetch_primary_data_source():
    """
    Simulates fetching data from the primary data source.
    Replace with actual implementation.
    """
    # Simulate a failure
    raise DataSourceUnavailable("Primary data source is unavailable.")

def fetch_secondary_data_source():
    """
    Simulates fetching data from the secondary (fallback) data source.
    Replace with actual implementation.
    """
    return "Data from secondary source"

def get_data():
    """
    Fetches data, falling back to a secondary source if the primary source is unavailable.
    """
    try:
        return fetch_primary_data_source()
    except DataSourceUnavailable:
        return fetch_secondary_data_source()

# Example usage
if __name__ == "__main__":
    data = get_data()
    print(f"Fetched data: {data}")
