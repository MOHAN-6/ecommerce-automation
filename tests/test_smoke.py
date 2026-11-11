from pages.product_page import ProductPage
from playwright.sync_api import expect

def test_guest_can_add_to_cart(authenticated_page):
    # 1. Navigate directly to the specific product page (Sauce Labs Backpack)
    authenticated_page.goto("https://www.saucedemo.com/inventory-item.html?id=4")
    
    # 2. Use our Page Object to add to cart
    product = ProductPage(authenticated_page)
    product.add_to_cart()
    
    # 3. Verify the cart badge shows 1
    expect(authenticated_page.locator(".shopping_cart_badge")).to_have_text("1")
def test_locked_out_user_cannot_login(page):
    # 1. Go to the login page
    page.goto("https://www.saucedemo.com/")
    
    # 2. Enter the locked out user credentials
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    # 3. Assert the error message appears
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_contain_text("Epic sadface: Sorry, this user has been locked out.")