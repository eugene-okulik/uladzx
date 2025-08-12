from .base_page import BasePage
from .locators import sale_page_locators as loc


class Sale(BasePage):
    page_url = '/sale.html'

    def check_if_deal_titles_are_correct(self,
                                         womens_text,
                                         mens_text,
                                         gears_text):
        womens = self.find(loc.womens_deals_loc)
        mens = self.find(loc.mens_deals_loc)
        gears = self.find(loc.gear_deals_loc)

        womens_actual = womens.inner_text()
        mens_actual = mens.inner_text()
        gears_actual = gears.inner_text()

        assert womens_actual == womens_text, f"Expected '{womens_text}', but got '{womens_actual}'"
        assert mens_actual == mens_text, f"Expected '{mens_text}', but got '{mens_actual}'"
        assert gears_actual == gears_text, f"Expected '{gears_text}', but got '{gears_actual}'"

    def check_the_sale_page_header_text(self, text):
        self.check_the_text(expected_text=text, locator=loc.sale_page_title_loc)

    def check_the_shipping_info_text(self, text):
        element = self.scroll_to_element(locator=loc.shipping_is_free_loc)
        actual_text = element.text_content().replace('\u00A0', ' ').strip()
        expected_text = text.replace('\u00A0', ' ').strip()
        assert actual_text == expected_text, f"Expected '{expected_text}', got '{actual_text}'"
