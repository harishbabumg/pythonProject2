from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()
driver.get("https://padakanaja.karnataka.gov.in/dictionary")
time.sleep(2)
driver.find_element_by_xpath("//select[@name='seldictionary']").click()
time.sleep(2)
driver.find_element_by_xpath("//option[text()='ಕನ್ನಡ ರತ್ನಕೋಶ |  "
                                 "ಕನ್ನಡ-ಕನ್ನಡ | ಪ್ರಕಾಶಕರು - ಕನ್ನಡ ಅಭಿವೃದ್ಧಿ ಪ್ರಾಧಿಕಾರ (1994)']").click()

"""taking more than 5 minutes"""
text_find = "ಅಂಕ"
# for _ in range(0, 93):
#     time.sleep(2)
#     driver.find_element_by_xpath("//option[@value='200']").click()
#     time.sleep(3)
#     result = driver.find_element_by_xpath(f"//td[text()='{text_find}']").text
#     if str(result) == str(text_find):
#         mean = driver.find_element_by_xpath(f"//td[text()='{text_find}']/..")
#
# #     driver.find_element_by_xpath("//a[@class='paginate_button next']").click()
# # print(result)
#
# print(mean)



list_ = []
for n in range(2, 11):
    time.sleep(2)
    driver.find_element_by_xpath("//option[@value='200']").click()
    time.sleep(3)
    result = driver.find_element_by_xpath(f"(//tr[@role='row'])[{n}]").text
    result.split()
    list_.append(result)
    # driver.find_element_by_xpath("//a[@class='paginate_button next']").click()  # clicks next button
driver.close()
# print(type(result))
dd = {}
for element in list_:
    st = element.split(" ")
    # a, *rest, b = st
    # print(st)
    for char in st:
        dd[st[0]] = str(st[1: -1])
print(dd)
