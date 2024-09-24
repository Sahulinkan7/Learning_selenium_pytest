from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

## find element by CLASS
driver.find_element(By.CLASS_NAME,"login_container").screenshot("01_no_credential_login.png")
## find element by ID

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")

## find element by CLASS
driver.find_element(By.CLASS_NAME,"login_container").screenshot("02_with_credential_login.png")

## find element by ID
driver.find_element(By.ID,"login-button").click()
print(driver.current_url)
time.sleep(2)
driver.find_element(By.CLASS_NAME,"inventory_container").screenshot("03_after_login.png")

## By CLASS NAME
products_quantity=driver.find_elements(By.CLASS_NAME,"inventory_item")
print("No of products shown in this page : ",len(products_quantity))

## By TAG NAME
product_details=products_quantity[0].find_elements(By.TAG_NAME,"div")
print(product_details)

## By CSS selector
products_css=driver.find_elements(By.CSS_SELECTOR,"div.inventory_item")

print(len(products_css))

## By Link Text
link=driver.find_element(By.LINK_TEXT,"Sauce Labs Backpack")
print("link text details",link)


partial_link=driver.find_element(By.PARTIAL_LINK_TEXT,"Labs")
print("by partial link text",partial_link)
print("partial link full text : ",partial_link.find_element(By.TAG_NAME,"div").text)

## By attribute

price=driver.find_element(By.CSS_SELECTOR,"[data-test=inventory-item-price]").text
print(price)

## By tagname,id , class 
item3_name=driver.find_element(By.CSS_SELECTOR,"#item_3_title_link[data-test='item-3-title-link']").find_element(By.CSS_SELECTOR,"div[data-test='inventory-item-name']").text
print("item3",item3_name)
time.sleep(7)
driver.close()