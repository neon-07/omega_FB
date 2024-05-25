import requests
from bs4 import BeautifulSoup
import re

# Define the URL of the webpage to scrape
url = 'https://pm-bet.in'

# Fetch the HTML content of the webpage
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all HTML elements containing phone numbers (adjust the selector as needed)
phone_elements = soup.find_all(string=re.compile(r'\b\d{10}\b|\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'))

# Extract the phone numbers from the HTML elements
phone_numbers = [phone.strip() for phone in phone_elements if re.search(r'\b\d{10}\b|\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', phone)]

# Print or further process the extracted phone numbers
for phone in phone_numbers:
    print(phone)
    
