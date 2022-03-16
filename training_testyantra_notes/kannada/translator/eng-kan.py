import time

from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
import re
from selenium.common.exceptions import NoSuchElementException
# From kannada.py

# parisaradha_kathe_3 = " ಅನಂತತೆ, ಲೀನವಾಗಿದೆ, ಸೋಜಿಗ, ಆನುಷಂಗಿಕ, ಗೋಜಿಗೆ, ನಿಶಿದ್ಧ, ಕಟ್ಟಳೆ, ಕಟ್ಟಾ, ಜಾತ್ಯಾತೀತ, " \
#                       "ಧೋರಣೆ, ತಳೆ, ತಾತ್ವಿಕವಾಗಿ, ಚರಾಚರ, ಸರ್ವಭಕ್ಷಕ, ಸಂಕ್ಷಿಪ್ತವಾಗಿ, ಪಂಥಿ, ನಿಸ್ಸಂಶಯವಾಗಿ, ಎಕ್ಕುಟ್ಟಿ ಹೋಗು, " \
#                       "ಸ್ವಾರಸ್ಯ, ಪುಳ್ಚಾರಿ ಊಟ, ಬೇಳೆತೊವ್ವೆ, ಜುಗುಪ್ಸೆ, ಸಂಚು, ಮುನ್ನುಡಿ, ತುರ್ತುಪರಿಸ್ಥಿತಿ, ಆರೋಪಿಸು, ಕರಾರುವಾಕ್ಕಾಗಿ, " \
#                       "ಮನದಟ್ಟಾಗಿ, ಧಡಾಕಿ, ಸಲಾಕಿ, ಗಡಚಿಕ್ಕುವಂಥ, ಆಸ್ಫೋಟನೆ, ದಟ್ಟಣಿ, ಅಸಂಖ್ಯಾತ, ಕಾಡು ಕೋಳಿ, ಕಾಡು ಕುರಿ, " \
#                       "ಕಾಡು ಹಂದಿ, ತರುವಾಯ, ನಿಟ್ಟುಸಿರು, ಶೋಕ, ಹರಟೆ, ತಾರೆ ಮರ, ವ್ಯೂಹ, ವ್ಯತಿರಿಕ್ತ, ಸೆಖೆ, ಬಿಕಾರಿ, ಕಾರ್ಪಣ್ಯ, " \
#                       "ವಾಟೆ ಬಿದಿರು, ಚಿಟ್ಟು ಕೋಳಿ, ಬೇಗೆ, ಇಂಗು, ವಾಟೆ ಬೊಂಬಿನ ಬಲೆ-ಬಲೆ ನೆರಳು, ಪ್ರಚೋದಿಸು, ಗುರುಗುಟ್ಟುತ್ತ, " \
#                       "ಮಗ್ಗುಲಿಗೆ, ತಾರಸ್ವರ, ಶಿಲಾಮೂರ್ತಿ,ಸಂಜ್ಞೆ, ಎರಡು ಮಾರು, ಕೌಚಿ, ನಾಗಲೋಟ, ಹಠಾತ್ತನೆ, ಕ್ಷಣಾರ್ಧದಲ್ಲಿ, " \
#                       "ಸಾಮರ್ಥ್ಯ, ಮೇರೆ ಮೀರಿ, ಅಸಹನೆ, ನಿರಾಶೆ, ಆಚೆಮಗ್ಗಲು, ಕಾರ್ಯಶೀಲ, ಚರ್ಯೆ, ಪಿಸುಮಾತು, ಶವಸದೃಶ, ಗಂಧಕ"

# res = parisaradha_kathe_3.split(",")
# ress= []
# for char in res:
#     if char[0] == " ":
#         ress.append(char[1:])
#     else:
#         ress.append(char)

# #
driver = webdriver.Chrome("./chromedriver")
keys = "Consequence Parrot Watch ಕಲೆ gksvckhgac horse cat hvcjksv book kangaroo"
# keys = "Consequence carnivores"
text = keys.split(" ")
dd = {}
# lst = []
# # #
driver.get("http://www.google.com")
driver.maximize_window()
driver.get("https://www.shabdkosh.com/dictionary/english-kannada/")
# for char in ress:
for char in text:
    driver.find_element_by_id("e").send_keys(char)
    time.sleep(1)
    driver.find_element_by_xpath("//button[@class='search-submit btn btn-primary px-3']").click()
    time.sleep(1)
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

