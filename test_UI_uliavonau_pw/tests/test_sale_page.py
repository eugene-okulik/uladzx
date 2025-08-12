def test_check_the_deal_titles(sale_page):
    sale_page.open_page()
    sale_page.check_if_deal_titles_are_correct(
        "Women's Deals",
        "Mens's Deals",
        "Gear Deals"
    )


def test_check_if_page_title_is_correct(sale_page):
    sale_page.open_page()
    sale_page.check_the_sale_page_header_text('Sale')


def test_check_if_free_shipping_info_displays(sale_page):
    sale_page.open_page()
    sale_page.check_the_shipping_info_text('Spend $50 or more — shipping is free!')
