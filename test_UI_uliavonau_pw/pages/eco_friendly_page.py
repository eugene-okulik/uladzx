from .base_page import BasePage
from .locators import eco_friendly_locators_page as loc


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def select_view(self, view_type: str):
        if view_type == "grid":
            view_btn = self.page.locator(loc.grid_btn)
        elif view_type == "list":
            view_btn = self.page.locator(loc.list_btn)
        else:
            raise ValueError("view_type must be 'grid' or 'list'")

        view_btn.evaluate("el => el.scrollIntoView({ block: 'center', behavior: 'auto' })")

        view_btn.wait_for(state="visible")

        view_btn.click()
        return view_btn

    def assert_display_type(self, view_type: str, expected_display: str):
        if view_type == "grid":
            container = self.find(loc.grid_container)
        elif view_type == "list":
            container = self.find(loc.list_container)
        else:
            raise ValueError("view_type must be 'grid' or 'list'")

        actual_display = container.evaluate("el => getComputedStyle(el).display")

        assert actual_display == expected_display, (
            f"Expected display: '{expected_display}' for view '{view_type}', but got: '{actual_display}'"
        )

        return actual_display

    def select_element_from_the_dropdown_and_check_items_display(self, text):
        dropdown = self.find(loc.dropdown_list)
        dropdown.select_option(label=text)

        sorter_btn = self.scroll_to_element(loc.sorter_btn)
        sorter_btn.click()

        item_1 = self.find(loc.first_product)
        item_2 = self.find(loc.second_product)

        price_text_1 = item_1.inner_text()
        price_text_2 = item_2.inner_text()

        price_value_1 = float(price_text_1.replace("$", "").strip())
        price_value_2 = float(price_text_2.replace("$", "").strip())

        sorter_btn_title = self.get_attribute(loc.sorter_btn, "title")

        if sorter_btn_title == "Set Descending Direction":
            assert price_value_1 < price_value_2, "Expected ascending order, but got descending."
        elif sorter_btn_title == "Set Ascending Direction":
            assert price_value_1 > price_value_2, "Expected descending order, but got ascending."
        else:
            raise ValueError(f"Unexpected sorter title: {sorter_btn_title}")
