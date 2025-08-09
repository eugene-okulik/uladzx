def test_products_displayed_as_grid(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.select_view("grid")
    eco_friendly_page.assert_display_type("grid", expected_display="block")


def test_products_displayed_as_list(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.select_view("list")
    eco_friendly_page.assert_display_type("list", expected_display="block")


def test_select_price_option_in_the_dropdown_list(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.select_element_from_the_dropdown_and_check_items_display(text="Price")
