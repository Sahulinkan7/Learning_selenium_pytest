from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()


driver.get("https://www.google.com")

search_input=driver.find_element(By.XPATH,"//*[@id='APjFqb']")
search_input.send_keys("Selenium")
search_input.submit()

ele=driver.find_element(By.XPATH,"//*[@id='rso']/div[6]/div/div/div[1]/div/div/div[1]/a/div/div[2]/div")
print(ele)
ele
time.sleep(3)
driver.quit()