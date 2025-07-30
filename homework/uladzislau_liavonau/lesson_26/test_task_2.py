from playwright.sync_api import Page


def test_registration_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form#google_vignette')
    page.get_by_role("textbox", name="First Name").fill("Jane")
    page.get_by_role("textbox", name="Last Name").fill("Doe")
    page.get_by_role("textbox", name="name@example.com").fill("janedoe@gmail.com")
    page.locator("label:has-text('Female')").click()
    page.get_by_role("textbox", name="Mobile Number").fill("1233211231")

    # Data picker
    calendar_input = page.locator("#dateOfBirthInput")
    calendar_input.click()
    calendar_input.press("Control+a")
    calendar_input.press("Backspace")
    calendar_input.fill("01 Jan 2000")
    calendar_input.press("Enter")

    # Subjects field
    subjects_loc = page.locator("#subjectsInput")
    subjects_loc.click()
    subjects_loc.fill("M")
    calendar_input.press("Enter")

    # Checkbox
    page.locator("label:has-text('Reading')").click()

    page.get_by_role("textbox", name="Current Address").fill("pr. Skaryny 123")

    # State drop-down
    page.locator("#state").click()
    page.locator(".css-yt9ioa-option").first.click()

    # City drop-down
    page.locator("#city").click()
    page.locator(".css-yt9ioa-option").first.click()

    page.get_by_role("button", name="Submit").click()
