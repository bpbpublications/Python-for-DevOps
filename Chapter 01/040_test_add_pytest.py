# Function to add two values
def add(a, b):
    """
    Returns the sum of a and b. Supports both numeric addition and string concatenation.
    """
    return a + b

# Test function for the add() function
def test_add():
    """
    Tests the add() function with various inputs.
    """
    # Test numeric addition
    assert add(2, 3) == 5, "Addition of integers failed."
    
    # Test string concatenation
    assert add('space', 'ship') == 'spaceship', "String concatenation failed."

    # Test float addition
    assert add(1.5, 2.5) == 4.0, "Addition of floats failed."
