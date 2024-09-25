from selenium import webdriver 
import time 

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.facebook.com")
driver.get("https://amazon.in")

time.sleep(2)
driver.back()
time.sleep(1)
driver.get("https://www.github.com/")
driver.back()
time.sleep(1)
driver.forward()
time.sleep(3)
driver.refresh()