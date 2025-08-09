import pytest
from playwright.sync_api import sync_playwright
from pages.create_customer_account_page import CreateCustomerAccount
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import Sale


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture()
def create_customer_account_page(page):
    return CreateCustomerAccount(page)


@pytest.fixture()
def sale_page(page):
    return Sale(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendly(page)
