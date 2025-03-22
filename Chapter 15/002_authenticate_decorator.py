# Script: 002_authenticate_decorator.py

# Decorator to check user authentication before executing a function
def authenticate_decorator(func):
    """
    A decorator to ensure the user is authenticated before calling the function.
    """
    def wrapper(user, *args, **kwargs):
        if not hasattr(user, 'is_authenticated') or not user.is_authenticated:
            raise Exception("Authentication required")
        return func(user, *args, **kwargs)
    return wrapper

@authenticate_decorator
def secure_function(user):
    """
    A secure function that requires an authenticated user.
    """
    print("Secure function execution")

# Example usage
if __name__ == "__main__":
    # Creating a mock user object with an `is_authenticated` attribute
    user = type('User', (object,), {"is_authenticated": True})()
    
    try:
        secure_function(user)
    except Exception as e:
        print(f"Error: {e}")
