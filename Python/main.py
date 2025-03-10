from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
#os.environ['PATH']+=r"C:/Program Files (x86)"
PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://tutorialsninja.com/demo/")

search = driver.find_element(By.CLASS_NAME,"price")
print(search.text)
time.sleep(6)