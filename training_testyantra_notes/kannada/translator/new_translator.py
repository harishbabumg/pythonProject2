from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("./chromedriver")
text = "ಇತಿಹಾಸ ಸಾಹಿತ್ಯ"
keys = text.split(" ")
dd = {}
for element in keys:
    driver.get("https://www.shabdkosh.com/dictionary/english-kannada/")
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@id='e']").send_keys(element)
    driver.find_element_by_xpath("//button[@class='search-submit btn btn-primary px-3']").click()
    WebDriverWait(driver, 20)
    try:
        if driver.find_element_by_xpath("//div[@class='col-sm-12 dc p-0']"):
            result = driver.find_element_by_xpath("//div[@class='col-sm-12 dc p-0']").text
            result = result.replace("\n", " ")
            dd[element] = result
        else:
            pass
    except NoSuchElementException:
        dd[element] = "None"

print(dd)





