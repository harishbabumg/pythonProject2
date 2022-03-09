
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
import re
# #
driver = webdriver.Chrome("./chromedriver")
keyss = "ಇತಿಹಾಸ - ಕರ್ನಾಟಕದ ಇತಿಹಾಸದಲ್ಲಿ ಸಾಹಿತ್ಯ, ಕಲೆ ಮತ್ತು ಶಿಲ್ಪಕಲೆಗಳಿಗೆ ಹೊಯ್ಸಳರ ಕೊಡುಗೆ ಅಪಾರ"
keys = "ಇತಿಹಾಸ ಕಲೆ ಕೊಡುಗೆ ಸಾಹಿತ್ಯ"
text = keys.split(" ")
print(text)
#
dd = {}
# lst = []
# # #
for char in text:
    driver.get("http://www.google.com")
    driver.get("https://www.shabdkosh.com/dictionary/english-kannada/")
    driver.find_element_by_id("e").send_keys(char)
    driver.find_element_by_xpath("//button[text() = 'Search']").click()
    if driver.find_element_by_xpath("//ol[@class=' eirol']/../.."):
        res = driver.find_element_by_xpath("//ol[@class=' eirol']/../..").text
        res = res.replace("\n", " - ")
        dd[char] = res
        # lst.append((char, res))
    else:
        dd[char] = None
#
print(dd)
# print(lst)



