from selenium import webdriver
import time 

from selenium.webdriver.common.by import By 

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.current_url)
time.sleep(10)


driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
time.sleep(10)

print(driver.current_url)
time.sleep(4)
# driver.close()
driver.quit()

