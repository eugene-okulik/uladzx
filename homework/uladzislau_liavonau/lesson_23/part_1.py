from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()

driver.get('https://www.qa-practice.com/elements/input/simple')
input_field = driver.find_element(By.XPATH, '//input[contains(@class, "form-control")]')
input_field.send_keys("test", Keys.ENTER)

wait = WebDriverWait(driver, 10)
result_window = wait.until(ec.visibility_of_element_located((By.XPATH, "//div//p[@class='result-text']")))

print("Printed text:", result_window.text)
