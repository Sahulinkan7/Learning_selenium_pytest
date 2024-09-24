from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.automationpractice.pl/index.php")

## XPATH
driver.find_element(By.XPATH,"//input[@id='search_query_top']").send_keys("shirt")
driver.find_element(By.XPATH,"//button[@name='submit_search' or class='btn btn-default button-search']").click()

## XPATH text()
driver.find_element(By.XPATH,"//a[text()='Women']").click()

## XPATH contains()
time.sleep(5)
driver.quit()