"""Chrome"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Navigate to Google.com
driver.get("https://www.google.com")

# First attempt:
"""driver.maximize_window()  # Maximize the browser window
driver.find_element(By.NAME, "q").send_keys("Hello, World!")  # Search for "Hello, World!"
time.sleep(5)
driver.find_element(By.NAME, "btnK").click()  # Click the Google Search button
time.sleep(8)"""

# Second attempt
webdriverWait(driver, 5).until(
    EC.presence_of_element_located((BY.CALSS8NAME, "gLFyf"))
)
input_element = driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("Hello, World!")
time.sleep(5)
btn1 = driver.find_element(By.CLASS_NAME, "gNO89b").click()
time.sleep(10)
# Close the browser
driver.quit()