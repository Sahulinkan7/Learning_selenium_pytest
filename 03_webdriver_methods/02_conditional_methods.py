from selenium import webdriver
import time 

from selenium.webdriver.common.by import By 

driver=webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")

searchelement=driver.find_element(By.XPATH,"//*[@id='search_query_top']")

print(searchelement.is_displayed())
print(searchelement.is_enabled())
print(searchelement.is_selected())

driver.close()

