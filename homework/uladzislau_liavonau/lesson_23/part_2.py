import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


options = Options()
driver = webdriver.Chrome()
driver.get('https://demoqa.com/automation-practice-form')


# "First name" field
first_name_field = driver.find_element(By.XPATH, '//input[@placeholder="First Name"]')
first_name_field.send_keys("Jane")

# "Last name" field
last_name_field = driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]')
last_name_field.send_keys("Doe")

# "Email" field
email_field = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
email_field.send_keys("janedoe@gmail.com")

# "Gender" radio button
gender_radio_button = driver.find_element(By.XPATH, '//label[@for="gender-radio-2"]')
driver.execute_script("arguments[0].scrollIntoView(true);", gender_radio_button)
driver.execute_script("arguments[0].click();", gender_radio_button)
gender_radio_button.click()

# "Mobile" field
mobile_field = driver.find_element(By.XPATH, '//input[@placeholder="Mobile Number"]')
mobile_field.send_keys("3752932222")

# "Date of birth" field
date_of_birth_field = driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]')
date_of_birth_field.send_keys(Keys.COMMAND + "a")
wait = WebDriverWait(driver, 10)
calendar = wait.until(ec.visibility_of_element_located(
    (By.XPATH, '//div//div[contains(@class, "react-datepicker__current-month")]'))
)
date_of_birth_field.send_keys("01 Jan 2025", Keys.ENTER)

# Subjects field
subjects_field = driver.find_element(By.XPATH, '//div[contains(@class, "subjects-auto-complete__value-container")]')
subjects_field.click()

input_inside = wait.until(
    ec.element_to_be_clickable(
        (By.XPATH, '//div[contains(@class, "subjects-auto-complete__input")]//input')
    )
)

input_inside.click()
input_inside.send_keys("M")

suggested_option = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Maths')]")))
suggested_option.click()

# "Music" checkbox
music_checkbox = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]')
music_checkbox.click()

# "Address" field
address_field = driver.find_element(By.XPATH, '//div//textarea[@id ="currentAddress"]')
address_field.send_keys("Address Test")

# "State" dropdown
state_dropdown = driver.find_element(By.XPATH, "//div//div[@id='state']")
state_dropdown.click()

state_values = driver.find_elements(By.XPATH, '//div[contains(@class, "css-yt9ioa-option")]')

random_choice_state = random.choice(state_values)

driver.execute_script("arguments[0].scrollIntoView(true);", random_choice_state)

wait.until(ec.element_to_be_clickable(random_choice_state))
random_choice_state.click()

# "City" dropdown
city_dropdown = driver.find_element(By.XPATH, "//div//div[@id='city']")
city_dropdown.click()

city_values = driver.find_elements(By.XPATH, '//div[contains(@class, "css-yt9ioa-option")]')

random_choice_city = random.choice(city_values)

wait.until(ec.element_to_be_clickable(random_choice_city))
random_choice_city.click()

# "Submit" button
submit_button = driver.find_element(By.XPATH, "//div//button[@type='submit']")
submit_button.click()

# Submitted form
submitted_form = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='modal-body']")))
print(submitted_form.text)
