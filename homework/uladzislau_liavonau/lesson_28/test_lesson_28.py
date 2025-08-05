from playwright.sync_api import Page, Route, expect
import json


def test_iphone(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        full_body = response.json()
        full_body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "яблокофон 16 про"
        route.fulfill(body=json.dumps(full_body))

    page.route(
        '**/shop/api/digital-mat?path=library/step0_iphone/digitalmat',
        handle_route
    )

    page.goto('https://www.apple.com/shop/buy-iphone')

    page.locator('text=iPhone 16 Pro & >> nth=0').click()

    header = page.locator('h2.rf-digitalmat-overlay-header').first

    expect(header).to_have_text('яблокофон 16 про')
