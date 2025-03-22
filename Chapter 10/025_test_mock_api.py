# Script: 025_test_mock_api.py

from unittest.mock import MagicMock

def test_fetch_data():
    """
    Test case to mock an API call using MagicMock. Verifies that the mock fetch_data function
    returns the expected data.
    """
    # Create a mock API object
    mock_api = MagicMock()
    
    # Define the return value for the fetch_data method
    mock_api.fetch_data.return_value = {"key": "value"}
    
    # Assert that the mocked method returns the expected value
    assert mock_api.fetch_data() == {"key": "value"}

# This test can be executed using a test runner like pytest or unittest.
