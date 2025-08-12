def test_create_customer_account_when_email_already_used(create_customer_account_page):
    create_customer_account_page.open_page()
    create_customer_account_page.fill_create_new_customer_account_form(
        'Jane', 'Doe', 'janedoe0706@gmail.com', 'Janedoe123@', 'Janedoe123@'
    )
    create_customer_account_page.check_email_already_used_text(
        'There is already an account with this email address. '
        'If you are sure that it is your email address, click here to get your password and access your account.'
    )


def test_check_validation_when_password_and_confirm_password_values_arent_the_same(create_customer_account_page):
    create_customer_account_page.open_page()
    create_customer_account_page.fill_create_new_customer_account_form(
        'Jane', 'Doe', 'janedoe0706@gmail.com', 'Janedoe123@', 'Janedoe12345'
    )
    create_customer_account_page.check_passwords_arent_the_same_text(
        'Please enter the same value again.'
    )


def test_check_validation_when_any_required_field_is_empty(create_customer_account_page):
    create_customer_account_page.open_page()
    create_customer_account_page.fill_create_new_customer_account_form(
        '', 'Doe', 'janedoe0706@gmail.com', 'Janedoe123@', 'Janedoe123@'
    )
    create_customer_account_page.check_required_field_is_empty_text(
        'This is a required field.'
    )
