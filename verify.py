from selenium import webdriver
import pandas as pd
import requests
import time



loginurl = ('https://backv1.sportsmanager.app/signin')
secureurl = ('https://betav2.sportsmanager.app/dashboard')
payload = { 
        'userName' : 'fairbet01',   
        'password' : 'xz&86d&8zP>20v#*'
    }


r = requests.post(loginurl, data=payload)

r2 = requests.get(secureurl)
driver = webdriver.Chrome()
time.sleep(50)


