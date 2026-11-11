from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_btn = page.get_by_role("button", name="Checkout")
        self.cart_item_name = page.locator(".inventory_item_name")

    def verify_item_in_cart(self, expected_name: str):
        expect(self.cart_item_name).to_have_text(expected_name)

    def proceed_to_checkout(self):
        self.checkout_btn.click()