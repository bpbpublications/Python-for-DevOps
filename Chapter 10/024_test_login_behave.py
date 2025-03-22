# Script: 024_test_login_behave.py

from behave import given, when, then

@given("a user is on the homepage")
def step_given_user_on_homepage(context):
    """
    Given step to ensure the user is on the homepage.
    Opens the homepage URL in the browser.
    """
    context.browser.get("https://example.com")

@when("the user clicks the login button")
def step_when_user_clicks_login(context):
    """
    When step to simulate the user clicking the login button.
    This step needs to perform the click action on the login button.
    """
    login_button = context.browser.find_element_by_id("login-button")  # Replace with actual button locator
    login_button.click()

@then("the login page is displayed")
def step_then_login_page_displayed(context):
    """
    Then step to verify that the login page is displayed after the user clicks the login button.
    Verifies the title of the page after the action.
    """
    assert context.browser.title == "Login Page"
