from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
import re
from selenium.common.exceptions import NoSuchElementException

# #
driver = webdriver.Chrome("./chromedriver")
# keys = "Consequence Parrot Watch ಕಲೆ gksvckhgac horse cat hvcjksv book kangaroo"
keys = "Consequence kjd Consequence Parrot Watch ಕಲೆ gksvckhgac horse cat hvcjksv book kangaroo"
text = keys.split(" ")
dd = {}
# lst = []
# # #
for char in text:
    driver.get("http://www.google.com")
    driver.get("https://www.shabdkosh.com/dictionary/english-kannada/")
    driver.find_element_by_id("e").send_keys(char)
    driver.find_element_by_xpath("//button[text() = 'Search']").click()
    try:
        if driver.find_element_by_xpath("//ol[@class=' eirol']/../.."):
            res = driver.find_element_by_xpath("//ol[@class=' eirol']/../..").text
            res = res.replace("\n", " - ")
            dd[char] = res
    except NoSuchElementException:
        dd[char] = "Meaning not found"


# print(dd)


for pair in dd:
    a = pair
    b = dd[pair]
    print(a, "--->", b)

