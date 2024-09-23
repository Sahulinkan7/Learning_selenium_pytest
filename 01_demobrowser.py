from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

# manually downloading chrome web driver 
# service_obj=Service("path to chrome driver which version is same as the installed chrome version")
# driver=webdriver.Chrome(service_obj)
# driver.get("https://rahulshettyacademy.com")

# chrome driver service
# driver=webdriver.Chrome()  # checks chrome driver version in present system and download the chrome driver and opens Chrome.
# driver.get("https://rahulshettyacademy.com")
# print(driver.title)
# print(driver.current_url)

driver=webdriver.Edge()  # checks chrome driver version in present system and download the chrome driver and opens Chrome.
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)


time.sleep(5)