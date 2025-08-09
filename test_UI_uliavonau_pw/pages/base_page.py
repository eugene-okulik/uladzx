from playwright.sync_api import Page, Locator


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for this page class')

    def find(self, locator: str) -> Locator:
        return self.page.locator(locator).first

    def find_all(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def get_attribute(self, locator: str, attribute_name: str) -> str:
        return self.find(locator).get_attribute(attribute_name)

    def check_the_text(self, expected_text: str, locator: str):
        actual_text = self.find(locator).inner_text()
        assert expected_text == actual_text, f"Expected '{expected_text}', got '{actual_text}'"

    def scroll_to_element(self, locator: str) -> Locator:
        element = self.find(locator)
        element.scroll_into_view_if_needed()
        return element
