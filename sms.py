from selenium import webdriver
import pandas as pd
import requests
import time

driver = webdriver.Chrome()

loginurl = 'https://betav2.sportsmanager.app/signin'
secureurl = 'https://betav2.sportsmanager.app/dashboard'
payload = { 
        'userName' : 'fairbet01',   
        'password' : 'xz&86d&8zP>20v#*'
    }

r = requests.post(loginurl, data=payload)

driver.get(secureurl)

time.sleep(50)  # Add a delay to ensure the page is fully loaded

# Find the element by XPath
data = driver.find_element_by_xpath('//*[@id="__next"]/div/div/main/div/section/div[1]')

# Find elements within the 'data' element
title = data.find_element_by_xpath('.//div[1]/div/div[1]/h2').text
value = data.find_element_by_xpath('.//div[1]/div/div[2]').text

print(title, value)

# Close the browser
driver.quit()
