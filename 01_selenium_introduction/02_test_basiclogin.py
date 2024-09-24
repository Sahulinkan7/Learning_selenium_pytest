from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
print(driver.current_url)

driver.find_element(By.XPATH,'//*[@id="Email"]').clear()
driver.find_element(By.XPATH,'//*[@id="Email"]').send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")

driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()

time.sleep(9)
print(driver.title)

time.sleep(10)