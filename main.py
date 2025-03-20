#https://www.youtube.com/watch?v=NB8OceGZGjA&t=1231s
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#from anticaptchaofficial.recaptchav2proxyless import *
import os


driver = webdriver.Chrome()

# Navigate to Google.com
driver.get("https://www.google.com")

#login to google



# Select the search box
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("chaima bouchareb")
input_element.send_keys(Keys.ENTER)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Chaima Bouchareb")))
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Chaima Bouchareb")
link.click()
time.sleep(20)

driver.quit()