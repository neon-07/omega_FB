import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the login page
loginurl = 'https://betav2.sportsmanager.app/signin'
driver.get(loginurl)

try:
    # Wait for the username input to be present and interactable
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'userName'))
    )
    password_input = driver.find_element(By.NAME, 'password')

    # Fill the form and submit
    username_input.send_keys('fairbet01')
    password_input.send_keys('xz&86d&8zP>20v#*')
    password_input.send_keys(Keys.RETURN)

    # Wait for a potential successful login redirect
    time.sleep(5)

    # Check if we have been redirected back to the login page
    if driver.current_url == loginurl:
        print("Login failed, redirected back to login page.")
    else:
        print("Login successful, navigating to the dashboard.")

    # Navigate to the secure URL if login is successful
    secureurl = 'https://betav2.sportsmanager.app/dashboard'
    driver.get(secureurl)

    # Add a delay to observe the result
    time.sleep(10)  # Adjust as needed

finally:
    # Close the browser
    driver.quit()
