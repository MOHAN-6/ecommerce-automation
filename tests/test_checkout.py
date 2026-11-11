from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect

def test_complete_checkout_flow(fast_authenticated_page):
    # 1. Go straight to the product and add it to cart
    fast_authenticated_page.goto("https://www.saucedemo.com/inventory-item.html?id=4")
    product = ProductPage(fast_authenticated_page)
    product.add_to_cart()
    
    # 2. Go to the cart page
    fast_authenticated_page.locator(".shopping_cart_link").click()
    
    # 3. Verify the item is in the cart and checkout
    cart = CartPage(fast_authenticated_page)
    cart.verify_item_in_cart("Sauce Labs Backpack")
    cart.proceed_to_checkout()
    
    # 4. Fill out the checkout form
    checkout = CheckoutPage(fast_authenticated_page)
    checkout.fill_shipping_info("John", "Doe", "12345")
    
    # 5. Finish the order and verify success
    checkout.finish_checkout()
    checkout.verify_success()