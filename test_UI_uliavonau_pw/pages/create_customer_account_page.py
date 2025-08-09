from .base_page import BasePage
from .locators import create_customer_account_locators_page as loc


class CreateCustomerAccount(BasePage):
    page_url = '/customer/account/create/'

    def fill_create_new_customer_account_form(self,
                                              firstname,
                                              lastname,
                                              email,
                                              password,
                                              confirm_password):
        self.find(loc.first_name_field_loc).fill(firstname)
        self.find(loc.last_name_field_loc).fill(lastname)
        self.find(loc.email_field_loc).fill(email)
        self.find(loc.password_field_loc).fill(password)
        self.find(loc.confirm_password_field_loc).fill(confirm_password)
        self.find(loc.create_account_btn_loc).click()

    def check_email_already_used_text(self, text):
        self.scroll_to_element(locator=loc.user_already_exist_error_loc)
        self.check_the_text(expected_text=text, locator=loc.user_already_exist_error_loc)

    def check_passwords_arent_the_same_text(self, text):
        self.scroll_to_element(locator=loc.confirm_password_isnt_the_same_text)
        self.check_the_text(expected_text=text, locator=loc.confirm_password_isnt_the_same_text)

    def check_required_field_is_empty_text(self, text):
        self.scroll_to_element(locator=loc.required_field_text)
        self.check_the_text(expected_text=text, locator=loc.required_field_text)
