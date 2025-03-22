# Script: 022_test_math_operations.py

import pytest

def test_addition():
    """
    Test case for checking the addition of two numbers.
    Verifies that 1 + 1 equals 2.
    """
    assert 1 + 1 == 2

def test_subtraction():
    """
    Test case for checking the subtraction of two numbers.
    Verifies that 3 - 1 equals 2.
    """
    assert 3 - 1 == 2

# The tests can be executed with pytest by running 'pytest' in the command line.
