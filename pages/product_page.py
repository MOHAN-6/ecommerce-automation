from playwright.sync_api import Page, expect

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_btn = page.get_by_role("button", name="Add to cart")
        self.cart_count = page.locator('.shopping_cart_badge')

    def add_to_cart(self):
        self.add_to_cart_btn.click()

    def expect_cart_count(self, count: int):
        expect(self.cart_count).to_have_text(str(count))