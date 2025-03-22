import unittest

class TestMathOperations(unittest.TestCase):
    """
    Unit tests for basic math operations.
    """

    def test_addition(self):
        # Test case for addition
        self.assertEqual(1 + 1, 2, "Addition test failed.")

    def test_subtraction(self):
        # Test case for subtraction
        self.assertEqual(5 - 3, 2, "Subtraction test failed.")

    def test_multiplication(self):
        # Test case for multiplication
        self.assertEqual(3 * 4, 12, "Multiplication test failed.")

    def test_division(self):
        # Test case for division
        self.assertEqual(8 / 2, 4, "Division test failed.")

    def test_division_by_zero(self):
        # Test case for division by zero
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0

# Run the tests
if __name__ == '__main__':
    unittest.main()
