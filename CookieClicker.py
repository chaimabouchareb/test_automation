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
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]")))

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

time.sleep(3)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, cookie_id)))
                                
cookie = driver.find_element(By.ID, cookie_id)


while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        # managing the exception of the product not being a number
        if not product_price.isdigit():
            continue
            
        product_price = int(product_price)
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break