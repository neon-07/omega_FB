from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

loginurl = 'https://betav2.sportsmanager.app/signin'
secureurl = 'https://betav2.sportsmanager.app/dashboard'
payload = {
    'userName': 'fairbet01',
    'password': 'xz&86d&8zP>20v#*'
}

# Use Selenium to login
driver.get(loginurl)
username_input = driver.find_element_by_name('userName')
password_input = driver.find_element_by_name('password')
username_input.send_keys(payload['userName'])
password_input.send_keys(payload['password'])
driver.find_element_by_xpath('//button[@type="submit"]').click()

# Wait for the dashboard to load
WebDriverWait(driver, 10).until(EC.url_to_be(secureurl))

# Find the elements
data_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="data-element"]'))
)

for data_element in data_elements:
    title_element = data_element.find_element_by_xpath('.//h2')
    value_element = data_element.find_element_by_xpath('.//div[2]')
    print(title_element.text, value_element.text)

time.sleep(100)