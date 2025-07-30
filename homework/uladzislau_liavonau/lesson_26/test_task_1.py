from playwright.sync_api import Page


def test_login_form(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role("link", name="Form Authentication").click()
    page.get_by_role("textbox", name="username").fill("janedoe123")
    page.get_by_role("textbox", name="password").fill("123456@")
    page.get_by_role("button", name="Login").click()
