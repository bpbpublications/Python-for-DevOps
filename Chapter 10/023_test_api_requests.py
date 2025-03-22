# Script: 023_test_api_requests.py

import requests
import unittest

class TestAPI(unittest.TestCase):
    """
    Test suite for testing API endpoints using the requests library.
    """

    def test_get_request(self):
        """
        Test case for sending a GET request to the API and checking the response status code.
        Verifies that the status code of the response is 200 (OK).
        """
        response = requests.get("https://api.example.com/data")
        self.assertEqual(response.status_code, 200)

# Run the tests when this script is executed
if __name__ == "__main__":
    unittest.main()
