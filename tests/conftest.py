import pytest
import os
from playwright.sync_api import Page, Playwright

AUTH_FILE = "auth.json"

@pytest.fixture(scope="session")
def auth_state(playwright: Playwright):
    if os.path.exists(AUTH_FILE):
        return AUTH_FILE
        
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle") # WAIT FOR CLOUD TO LOAD
    
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    page.wait_for_url("**/inventory.html")
    page.wait_for_load_state("networkidle") # WAIT FOR CLOUD TO LOAD
    
    context.storage_state(path=AUTH_FILE)
    browser.close()
    return AUTH_FILE

@pytest.fixture
def fast_authenticated_page(playwright: Playwright, auth_state):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    
    page.goto("https://www.saucedemo.com/inventory.html")
    page.wait_for_load_state("networkidle") # WAIT FOR CLOUD TO LOAD
    
    yield page
    browser.close()