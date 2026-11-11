import pytest
import os
from playwright.sync_api import Page, Playwright

# Define where we will save the login session
AUTH_FILE = "auth.json"

@pytest.fixture(scope="session")
def auth_state(playwright: Playwright):
    """
    This runs ONCE per test session.
    It logs in via UI, saves cookies to auth.json, and then closes the browser.
    """
    # If the file already exists, just use it
    if os.path.exists(AUTH_FILE):
        return AUTH_FILE
        
    # CHANGED TO TRUE FOR CLOUD CI
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    # Perform the login
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/inventory.html")
    
    # Save the cookies and local storage to a file
    context.storage_state(path=AUTH_FILE)
    browser.close()
    
    return AUTH_FILE

@pytest.fixture
def fast_authenticated_page(playwright: Playwright, auth_state):
    """
    This fixture reuses the saved auth.json cookies. 
    It skips the login UI entirely and goes straight to the inventory.
    """
    # CHANGED TO TRUE FOR CLOUD CI
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    
    # We are already logged in!
    page.goto("https://www.saucedemo.com/inventory.html")
    
    yield page
    
    browser.close()