# # practice
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
import re
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://www.google.com")
# driver.get("https://www.shabdkosh.com/dictionary/english-kannada/")
# a = driver.find_element_by_id("e").send_keys("ಪ್ರಪಂಚ")
# b = driver.find_element_by_xpath("//button[text() = 'Search']").click()
# # mean = driver.find_element_by_xpath("//ol[@class=' eirol']/../..//a")
# mean = driver.find_element_by_xpath("//ol[@class=' eirol']/../..")
#
# res = mean.text, end=""


# keyss = "ಇತಿಹಾಸ - ಕರ್ನಾಟಕದ ಇತಿಹಾಸದಲ್ಲಿ ಸಾಹಿತ್ಯ, ಕಲೆ ಮತ್ತು ಶಿಲ್ಪಕಲೆಗಳಿಗೆ ಹೊಯ್ಸಳರ ಕೊಡುಗೆ ಅಪಾರ"
# keys = "ಇತಿಹಾಸ ಕಲೆ ಕೊಡುಗೆ"
# text = keys.split(" ")
# print(text)

# dd = {}
# lst = []
# #
# for char in text:
#     driver.get("http://www.google.com")
#     driver.get("https://www.shabdkosh.com/dictionary/english-kannada/")
#     driver.find_element_by_id("e").send_keys(char)
#     driver.find_element_by_xpath("//button[text() = 'Search']").click()
#     mean = driver.find_element_by_xpath("//ol[@class=' eirol']/../..")
#     res = mean.text
#     res = res.replace("\n", " ")
#     # dd[char] = res
#     lst.append((char, res))

# print(dd)
# print(lst)



questions = " Generators, stale element exception, Quality control and Quality assessment, Verification and Validation, pytest framework, SDLC, types of error, approach to write a test case, __init__, config, how do you locate element in popup, CSS locator compared to other locator, Alpha beta testing, Relative xpath and Abosulute xpath, heapleakage, Assertions, tuples and lists, versions of xpath, Mutability, immutability, adding two tuples, locating element with same xpath but difference browser, Global variable and local variable, sychronisation, challenges in automation, explicit wait, modules handled, exceptions handled, test suites, how do you connect the POM classes to rest of the test scripts, when application is given to you how to start automating it, when existing framework is given to how do you see the framework, why and when you use automation, your contribution in framework, How test case allotment happens your project for day to day automation, your current roles and responsibility in the project, Explain the framework or what kind of framework you are using, diff b/w mutable and immutable, pickling and unpickling, diff b/w ‘/’ and ‘//’, class used for mouse over, meetings conducted in agile methodology, advantages of Agile, program for prime num, iterators meaning, code to scroll down the page, range and xrange, comprehension definition, API testing, name spaces in python, difference between.py and .pyc, difference between list and dictionary, inbuilt data types, convert a number into string, monkey patching, what is inheritance?¸ what is polymorphism?, encapsulation?, tell brief about slicing?, what are keywords in python tell some example about that?, smoke and sanity testing?, tell about defect life cycle?, explain about frame work that related to your project?, you have 50 regression test cases you have to deploy the project tomorrow and you were only qa in your team how do you handle the situation?, you raised a defect and that defect was consultancy rejected by the developer how do you handle the situation?, question related to joins?, roles and responsibilities in your present company?, SDLC, STLC, member operators and other operators, WAP to count no of words  and Occurance of  word in a text file, Why  POM used, Mutable and immutable, extract value from dict, decorators, self and cls in class, about previous project, your frd sends a python file..  You don't have any pychram or vscode or any, How you will execute python file(answer. command prompt), create folder inside folder and a text file inside that and asked to access it, os module, arrays and list, 2nd maximum value in the dictionary using pattern matching...., python modules did you use in your project?, abstract clas, What is property and why do we use that?, Have you used any version control tool in your project?, Can you check the presence of a folder on your system through a program, Create a file using python script on your system, How do you push the code on github, Which are the libraries you used in python?, Get the repeated items from the list  in an ascending order, What are the opps concept you used in your project and why they are important?, decorator, one program on decorator which you used in your project and explain, one class example, _ init_ and why we use it, constructor, cicd tool you used in your project, Did you use threading?, How do you instantiate different browsers in pytest, How do you take screenshots in selenium, Explain about agile methodology, framework, do you use switchto in selenium, xpath explain in detail., implicitly wait, explicit wait, Tools used, Criteria for choosing a test case for automation, Cicd tool, Version control : common commands and what are the statuses, Have you worked on API - common commands in it?, POM, creating reports in your team, Criterias for creating a class, Brief OOPs, daily work related activities, debug in pycharm, relative and absolute x path what does * signifies in the relative x path?, listbox, action chains, can you do automation without manual testing?on wt basis u go fr automation?, membership &identity operator, How to run only failed test cases, merge two dict, Packing and unpacking, Difference between find element and find elements, How will start writing scripts, Return type of map, Lambda, tell me about @fixture, difference between yield and return, how to tackel the pop up message, about indentation, about conftest, Smoke test, sanity test,, encapsulated in ur project,, what I's @ property, polymorphism with examples, in git how to check that code u have add is correct or not, why tuple  has less memory consumption than list,, how u have done regression testing in ur project, how much hours it's taken..how did u run that., have u used synchronisation, Bug life cycle, Default dict, Grid, Action chain, Path, Group by method, Salenium architecture, about pytest, Explain Polling time, What is multithreading, Getter and setter, Pattern programming, why python is Object Oriented(because everything in python is an object)?, Polling time and Poll Frequency both are same, 1. pyc files are python compiled, 2. Once .py file is compiled by python compiler, it generates .pyc file, .pyc files contains byte code which is understandable by python virtual machine, pyc files are generated when a python module is imported, Deep copy and shallow copy, What is load test and stress test, How to generate random numbers in python?, How do you manage colors on a page?, How do you generate html reports?, How to execute python file on terminal?, Is it possible to automate double click?, How do you select 4th item from the google search list?, How does memory allocation happen in python?, Explain slicing,"
s = []
res = questions.split(",")
lens = len(s)
for question in res:
    s.append(question[1:])
# print(s)

for item in s:
    for _ in range(0, len(s)-1):
        print(f"{_}" + item)



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
