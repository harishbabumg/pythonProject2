# # practice
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
import re
#
driver = webdriver.Chrome("./chromedriver")
# driver.get("http://www.google.com")
# driver.get("https://www.shabdkosh.com/dictionary/english-kannada/")
# a = driver.find_element_by_id("e").send_keys("ಪ್ರಪಂಚ")
# b = driver.find_element_by_xpath("//button[text() = 'Search']").click()
# # mean = driver.find_element_by_xpath("//ol[@class=' eirol']/../..//a")
# mean = driver.find_element_by_xpath("//ol[@class=' eirol']/../..")
#
# res = mean.text, end=""


keyss = "ಇತಿಹಾಸ - ಕರ್ನಾಟಕದ ಇತಿಹಾಸದಲ್ಲಿ ಸಾಹಿತ್ಯ, ಕಲೆ ಮತ್ತು ಶಿಲ್ಪಕಲೆಗಳಿಗೆ ಹೊಯ್ಸಳರ ಕೊಡುಗೆ ಅಪಾರ"
keys = "ಇತಿಹಾಸ ಕಲೆ ಕೊಡುಗೆ"
text = keys.split(" ")
print(text)

dd = {}
lst = []
# #
for char in text:
    driver.get("http://www.google.com")
    driver.get("https://www.shabdkosh.com/dictionary/english-kannada/")
    driver.find_element_by_id("e").send_keys(char)
    driver.find_element_by_xpath("//button[text() = 'Search']").click()
    mean = driver.find_element_by_xpath("//ol[@class=' eirol']/../..")
    res = mean.text
    res = res.replace("\n", " ")
    # dd[char] = res
    lst.append((char, res))

# print(dd)
print(lst)








# Navigate to demoweshop


# driver.minimize_window()
# sleep(2)
# driver.maximize_window()
# sleep(2)
#
# current_title = driver.title
#
# url = driver.current_url
#
# print(current_title)
# print(url)
#
# d = driver.find_element_by_link_text("Register").click()
# sleep(2)
#
# driver.find_element_by_id("gender-male").click()
# sleep(2)
#
# driver.find_element_by_id("FirstName").send_keys('HB')
# sleep(2)
#
# driver.find_element_by_id("LastName").send_keys('MG')
# sleep(2)
#
# driver.find_element_by_id("Email").send_keys('hbmg00@gmail.com')
# sleep(2)
#
# driver.find_element_by_id("Password").send_keys('123456')
# sleep(2)
#
# driver.find_element_by_id("ConfirmPassword").send_keys('123456')
# sleep(2)
#
# driver.find_element_by_id("register-button").click()
# sleep(2)
#
# prices = "from $45154545 KK imjHvasjacb"
#
# for price in prices:
#     if price in ".+-0123456789":
#         res = "".join(price)
#         print(res, end="")
# print(res)
# a = int(res)
# print(type(a))
