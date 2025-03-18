from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/")
search = "scrapy tuto"
time.sleep(19)
mysearch = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]')
mysearch.send_keys(search)
btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
time.sleep(19)
