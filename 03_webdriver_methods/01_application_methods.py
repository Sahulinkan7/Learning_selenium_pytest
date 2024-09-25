from selenium import webdriver
import time 

from selenium.webdriver.common.by import By 

driver=webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")

print(driver.title)
print(driver.current_url)

contactelement=driver.find_element(By.XPATH,"//*[@id='contact-link']/a")
contactelement.click()

print(driver.current_url)

print(driver.page_source)

driver.quit()

