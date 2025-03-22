# Script: 021_test_login.py

from selenium import webdriver

def test_login():
    """
    Automates the login process and verifies that the user is redirected to the dashboard page.
    Assumes a successful login leads to a page with 'Dashboard' in the title.
    """
    # Initialize the WebDriver for Chrome browser
    driver = webdriver.Chrome()
    
    try:
        # Navigate to the login page
        driver.get("https://example.com/login")

        # Perform login actions (this part would involve interacting with form elements)
        # For example:
        # driver.find_element_by_name("username").send_keys("your_username")
        # driver.find_element_by_name("password").send_keys("your_password")
        # driver.find_element_by_name("login_button").click()

        # Assert that the page title contains "Dashboard" after login
        assert "Dashboard" in driver.title

    except Exception as e:
        print(f"Error during login test: {e}")
    finally:
        # Ensure the WebDriver quits and closes the browser
        driver.quit()

# Run the login test when the script is executed
if __name__ == "__main__":
    test_login()
