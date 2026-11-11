from pages.product_page import ProductPage
from playwright.sync_api import expect

def test_guest_can_add_to_cart(fast_authenticated_page):
    fast_authenticated_page.goto("https://www.saucedemo.com/inventory-item.html?id=4")
    product = ProductPage(fast_authenticated_page)
    product.add_to_cart()
    expect(fast_authenticated_page.locator(".shopping_cart_badge")).to_have_text("1")

def test_locked_out_user_cannot_login(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_contain_text("Epic sadface: Sorry, this user has been locked out.")