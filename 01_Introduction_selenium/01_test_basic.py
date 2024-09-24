from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.current_url)

time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
actual_title=driver.title
expected_title="OrangeHRM"

if actual_title==expected_title:
    print("Login test passed")
else:
    print("Login test failed")
    
time.sleep(3)

