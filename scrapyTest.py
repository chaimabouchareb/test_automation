from Selenium import webdriver  
import time  
from Selenium.webdriver.common.keys import Keys  
print("sample test case started")  
PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) 
#driver=webdriver.firefox()  
#driver=webdriver.ie()  
#maximize the window size  
driver.maximize_window() 
#navigate to the url  
driver.get("https://www.google.com/")  
#identify the Google search text box and enter the value  
driver.find_element_by_name("q").send_keys("javatpoint")  
time.sleep(3)  
#click on the Google search button  
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
time.sleep(3)  
#close the browser  
driver.close()  
print("sample test case successfully completed")  