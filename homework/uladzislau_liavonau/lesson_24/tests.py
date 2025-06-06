import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


# Add device to the cart
def test_add_selected_device_to_cart(driver):
    driver.get('https://www.demoblaze.com/index.html')

    wait = WebDriverWait(driver, 10)

    # Device selection and page opening in new tab
    device_link = wait.until(ec.visibility_of_element_located(
        (By.XPATH, '//a[@href="prod.html?idp_=2"]'))
    )
    selected_device = driver.find_element(
        By.XPATH, "//a[@class='hrefch' and contains(text(), 'Nokia')]"
    )
    selected_device_text = selected_device.text

    ActionChains(driver).key_down(Keys.COMMAND).click(device_link).key_up(Keys.COMMAND).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Add device to the cart
    add_to_cart_button = wait.until(ec.visibility_of_element_located(
        (By.XPATH, '//a[@onclick="addToCart(2)"]'))
    )
    add_to_cart_button.click()

    # Find and accept alert
    alert = Alert(driver)
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    alert.accept()

    # Return to the main page
    product_store_button = driver.find_element(By.XPATH, '//a[@class="navbar-brand"]')
    product_store_button.click()

    # Go to the cart
    cart_button = driver.find_element(By.XPATH, '//a[@href="cart.html"]')
    cart_button.click()

    # Device in the cart
    device_in_the_cart = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, '//td[text()="Nokia lumia 1520"]')
    )
    )
    device_in_the_cart.click()
    device_in_the_cart_name = device_in_the_cart.text

    # Results assertion
    assert selected_device_text == device_in_the_cart_name, \
        f"TEST FAILED: Values are not the same!"


def test_add_to_compare_items(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')

    wait = WebDriverWait(driver, 10)

    # Find the firt item
    first_product = wait.until(ec.presence_of_element_located(
        (By.XPATH, '(//a[@class="product-item-link"])[1]')
    )
    )
    selected_product_name = first_product.text

    actions = ActionChains(driver)
    actions.move_to_element(first_product).perform()

    compare_button = first_product.find_element(By.XPATH, "(//a[@class='action tocompare'])[1]")
    compare_button.click()

    # Wait until compare section is visible
    wait.until(
        ec.visibility_of_element_located(
            (By.XPATH, '//a[@class="action compare primary"]')
        )
    )

    # Find the item in the compare section
    remove_button = driver.find_element(By.XPATH, '//a[@title="Remove This Item"]')
    compare_section = remove_button.find_element(By.XPATH, './ancestor::li[contains(@class, "product-item")]')
    product_name_element = compare_section.find_element(By.XPATH, './/strong[@class="product-item-name"]/a')
    product_name = product_name_element.text

    assert selected_product_name == product_name, \
        f"TEST FAILED: Values are not the same!"
