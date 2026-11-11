from playwright.sync_api import Page, expect

def test_iframe_input(page: Page):
    # 1. Navigate to a page that has a text input INSIDE an iframe
    page.goto("https://the-internet.herokuapp.com/iframe")
    
    # 2. Target the iframe by its ID
    # Playwright's frame_locator is incredibly smart. 
    # It automatically waits for the iframe to load.
    iframe = page.frame_locator("#mce_0_ifr")
    
    # 3. Locate the text body INSIDE the iframe and click it
    # (The editor uses a body tag instead of a normal input)
    editor_body = iframe.locator("body")
    editor_body.click()
    
    # 4. Clear the existing text and type our own
    # keyboard.press("Control+A") selects all text, then we type over it
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    editor_body.fill("This text was typed INSIDE the iframe!")
    
    # 5. Verify the text is actually there
    expect(editor_body).to_contain_text("This text was typed INSIDE the iframe!")