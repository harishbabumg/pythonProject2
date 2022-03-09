# practice
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep

driver = webdriver.Chrome("./chromedriver")
driver.get("http://www.google.com")

# Navigate to demoweshop

driver.get("http://demowebshop.tricentis.com/")
driver.minimize_window()
sleep(2)
driver.maximize_window()
sleep(2)

current_title = driver.title

url = driver.current_url

print(current_title)
print(url)

# driver.close()

# html -> hyper text markup language

driver.find_element_by_link_text("Register").click()
driver.find_element_id("Gender-male").click()
