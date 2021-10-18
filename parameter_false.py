from playwright.sync_api import sync_playwright

def parameter_false():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            record_har_path='parameter_false.har',
            record_har_omit_content=False
            )
        page.goto("http://playwright.dev")
        page.close()
        browser.close()
