from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.zip_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_btn = page.get_by_role("button", name="Continue")
        self.finish_btn = page.get_by_role("button", name="Finish")
        self.success_header = page.locator(".complete-header")

    def fill_shipping_info(self, first_name: str, last_name: str, zip_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_code_input.fill(zip_code)
        self.continue_btn.click()

    def finish_checkout(self):
        self.finish_btn.click()

    def verify_success(self):
        expect(self.success_header).to_have_text("Thank you for your order!")