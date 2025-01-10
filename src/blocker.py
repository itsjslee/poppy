# script.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

# Set up the WebDriver (make sure to specify the correct path to your WebDriver)
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Function to check and modify the URL
def check_youtube_url():
    while True:
        current_url = driver.current_url
        if "youtube.com" in current_url and not current_url.endswith('.'):
            new_url = re.sub(r'(youtube\.com)', r'\1.', current_url)
            driver.get(new_url)
        time.sleep(5)  # Check every 5 seconds

# Open YouTube and start checking the URL
driver.get("https://www.youtube.com")
check_youtube_url()