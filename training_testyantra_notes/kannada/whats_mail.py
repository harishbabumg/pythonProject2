from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
import re
from selenium.common.exceptions import NoSuchElementException
import time


############################################
# list_ = []
# for char in range(1, 101):
#     res = f"ನಮಸ್ಕಾರ {repr(char)}ನೇ ಸಾರಿ"
#     list_.append(res)

# driver = webdriver.Chrome("./chromedriver")
# driver.maximize_window()
# driver.get("https://web.whatsapp.com/")
# time.sleep(10)
# driver.find_element_by_xpath("//div[@title='Search input textbox']").send_keys("7411135403")
# driver.find_element_by_xpath("(//span[@title='Nikhil'])[1]").click()
# for char in list_:
#     driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(char)
#     time.sleep(0)
#     driver.find_element_by_xpath("//span[@data-testid='send']").click()


# list_ = []
# for char in range(1, 101):
#     res = f"ನಮಸ್ಕಾರ {repr(char)}ನೇ ಸಾರಿ"
#     list_.append(res)
#
# driver = webdriver.Chrome("./chromedriver")
# driver.maximize_window()
# driver.get("https://web.whatsapp.com/")
# time.sleep(10)
# driver.find_element_by_xpath("//div[@title='Search input textbox']").send_keys("9538902998")
# driver.find_element_by_xpath("(//span[@title='ಚಂದನ Chandana TestYantra'])[1]").click()
# for char in list_:
#     driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(char)
#     # time.sleep(10)
#     driver.find_element_by_xpath("//span[@data-testid='send']").click()

# list_ = []
# for char in range(1, 101):
#     # res = f"ನಮಸ್ಕಾರ {repr(char)}ನೇ ಸಾರಿ"
#     res = f"ನಾಷ್ಟ ಮಾಡು, {repr(char)}ನೇ ಸಾರಿ"
#     list_.append(res)
#
# driver = webdriver.Chrome("./chromedriver")
# driver.maximize_window()
# driver.get("https://web.whatsapp.com/")
# time.sleep(45)
# driver.find_element_by_xpath("//span[@data-icon='chat']").click()
# time.sleep(5)
# driver.find_element_by_xpath("(//div[@title='Search input textbox'])[1]").send_keys("+91 9663147807")
# time.sleep(5)
# driver.find_element_by_xpath("(//span[@title='Amma ಅಮ್ಮ'])[1]").click()
# for char in list_:
#     driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(char)
#     driver.find_element_by_xpath("//span[@data-testid='send']").click()

list_ = []
for char in range(1, 101):
    # res = f"ನಮಸ್ಕಾರ {repr(char)}ನೇ ಸಾರಿ"
    res = f"ನಾಷ್ಟ ಮಾಡು, {repr(char)}ನೇ ಸಾರಿ"
    list_.append(res)

driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
time.sleep(120)
driver.find_element_by_xpath("//span[@data-icon='chat']").click()
time.sleep(15)
driver.find_element_by_xpath("(//div[@title='Search input textbox'])[1]").send_keys("Meena A")
time.sleep(15)
driver.find_element_by_xpath("(//span[@title='Meena A'])[1]").click()
for char in list_:
    driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(char)
    time.sleep(10)
    driver.find_element_by_xpath("//span[@data-testid='send']").click()
