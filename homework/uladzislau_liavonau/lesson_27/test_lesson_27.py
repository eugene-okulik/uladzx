from playwright.sync_api import Page, expect, BrowserContext

# Task 1
def test_check_the_alert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.on('dialog', lambda alert: alert.accept())
    page.get_by_role('link', name='Click').click()
    result_message = page.locator("#result-text")
    expect(result_message).to_have_text("Ok")

# Task 2
def test_check_if_a_new_tab_appears(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    link = page.get_by_role('link', name='Click')

    with context.expect_page() as new_page_event:
        link.click()

    new_page = new_page_event.value
    result_message = new_page.locator('#result-text')
    expect(result_message).to_have_text("I am a new page in a new tab")

# Task 3
def test_wait_when_the_button_color_text_is_red(page: Page):
    page.goto('https://demoqa.com/dynamic-properties#google_vignette')
    color_button = page.locator('#colorChange')
    expect(color_button).to_contain_class('mt-4 text-danger btn btn-primary')
