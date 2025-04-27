import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


options = Options()
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


# Task 3.1
def test_elements_assertion():
    driver.get("https://www.qa-practice.com/elements/select/single_select")

    choose_language_field = driver.find_element(By.XPATH, "//div//select[@class='form-select']")
    choose_language_field.click()

    language_values = driver.find_elements(By.XPATH, "//div//select//option")
    random_selected_languge = random.choice(language_values)
    expected_language_value = random_selected_languge.text

    wait.until(ec.element_to_be_clickable(random_selected_languge))
    random_selected_languge.click()

    submit_button = driver.find_element(By.XPATH, "//div//input[@type='submit']")
    submit_button.click()

    you_selected_form = wait.until(ec.visibility_of_element_located((By.XPATH, "//div//p[@id='result-text']")))
    actual_language_value = you_selected_form.text

    assert expected_language_value == actual_language_value, "Values don't match!"


# Task 3.2
def test_check_if_helloworld_appears():
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = driver.find_element(By.XPATH, "//div//button")
    start_button.click()

    hello_world_element = wait.until(ec.visibility_of_element_located((By.XPATH, "(//div//div//h4)[2]")))
    hello_world_text = hello_world_element.text

    assert hello_world_text == "Hello World!", "'Hello World!' text not found"
