from selenium import webdriver 
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")

name=driver.find_element(By.XPATH,"//*[@id='block_top_menu']/ul/li[2]/a/self::a").text

print(name)