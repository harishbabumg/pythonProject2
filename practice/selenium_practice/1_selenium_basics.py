import time
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
# driver = webdriver.Chrome("./chromedriver")
# driver.get("https://www.google.co.in/")


# Common browser actions

# driver.maximize_window()
# driver.refresh()
# driver.minimize_window()

# current_title = driver.title
# print(current_title)
# url = driver.current_url
# print(url)

# driver.get("https://www.google.co.in/")
# driver.quit()
# driver.close()

"""
CSS Selector syntax = HTMLTAG[attribute=‘attribute_value’] ex. input[id='gender-male’]
Xpath syntax = //HTMLTAG[@attribute='value’]
    Absolute xpath, ex. /html/body/div[1]/div/div[2]/span/input
    Relative xpath, ex. //input[@id='newsletter-email’]
    text, ex. //a[text()=‘Register’] 
contains() function is useful when we want to match the value of any attribute partially.
    It can be used when the value of any attribute changes dynamically.
    also used to match an element if the attribute value has leading and/or trailing white spaces.
    syntax, ex. //a[contains(text(),‘Python Jobs’)]
            ex. //input[contains(@name,‘spam’)]
Indexing
    ex. (//input[@name=‘Gender’])[1]
    ex. (//input[@name=‘Gender’])[2]

"""
# To check the checkboxes
# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
# driver.maximize_window()

# languages = ['Ruby', 'Java', 'Perl', 'Python', 'C#', 'JavaScript']
# for language in languages:
#     driver.find_element_by_xpath(f"//td[text()='{language}']/..//input[@name='download']").click()
#     time.sleep(2)

# sample
"""
Dynamic XPath is also called as custom XPath and it is one way to locate element uniquely.
Dynamic XPath is used to locate exact attribute or 
decrease the number of matching nodes/result from a webpage
"""
# books = ['Computing and Internet', 'Fiction', 'Health Book']
# driver = webdriver.Chrome("./chromedriver")
# time.sleep(10)
# driver.get("http://demowebshop.tricentis.com/books")
# driver.maximize_window()
#
# for book in books:
#     time.sleep(3)
#     driver.find_element_by_xpath(f"//a[text()='{book}']/../..//input[@value='Add to cart']").click()
#     time.sleep(3)
# driver.get("http://demowebshop.tricentis.com/cart")  # checking the check box
# for book in books:
#     time.sleep(3)
#     driver.find_element_by_xpath(f"//a[text()='{book}']/../..//input[@type='checkbox']").click()

# clicking on radio button

# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# ratings = ["Excellent", "Good", "Poor", "Very bad"]
# for rating in ratings:
#     driver.find_element_by_xpath(f"//label[text()='{rating}']/..//input[@type='radio']").click()
#     time.sleep(2)

"""
Parent-Child relationship
    //input matches all the input elements in the
    entire webpage
    //div[@name=‘login’]//input matches all
    the input elements under the division(div) “login”
    //div[@name=‘login’]/input matches all the
    input elements which are immediate children of
    division “login”
    
    Double forward slash “//” denotes any child.
    Single forward slash “/” denotes immediate child.

"""
# VALIDATE THE ACTUAL PRICES OF ALL THE BOOKS AGAINST THE EXPECTED PRICE

"""Not working as expected"""
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/books")
# driver.maximize_window()
# expected_prices = {"Science": 51.00, "Health Book": 10.00, "Computing and Internet": 10.00, "Fiction": 24.00}
# for book,expected_price in expected_prices.items():
#     actual_price= driver.find_element_by_xpath("//a[text()='Fiction']/../..//span[@class='price actual-price']").text
#     if float(actual_price) == expected_price:
#         print("pass")
#     print("fail")
#     print(f"the expeted price of the {book} was {expected_price} but displaying {actual_price}")

"""
LOCATING MULTIPLE ELEMENTS
find_elements
    Returns list of web elements.
    Each item of the list is a web element.
    If there are no web elements which matches the given property and its value, find_elements
    method returns an empty list.
    
"""
# clicking on checkboxes
# driver = webdriver.Chrome('chromedriver')
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
# elements = driver.find_elements_by_name("download")
#
# for element in elements:
#     element.click()

# writing on mutiple text boxes
# driver = webdriver.Chrome('chromedriver')
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
# boxes = driver.find_elements_by_xpath("//input[@name='fname']")
# contents = ["Hello", "HB", "World", "Universe", "Python", "HB", "World", "Universe", "World"]
# for box, content in zip(boxes, contents):
#     box.send_keys(f"{content}")

# getting all links
# driver = webdriver.Chrome('chromedriver')
# driver.get("https://www.python.org/")
# elements = driver.find_elements_by_xpath("//a")
# for element in elements:
#     print(element.text)

"""
SELECT ELEMENT
    All list box related methods are implemented inside the class “Select”.
    In order to access methods of ”Select” class, we need to create an object instance to the
    ”Select” class and pass a “WebElement” (list box) as constructor argument.
    3 different methods available in “Select” class
        1. select_item_by_visible_text
            select_by_visible_text Selects an
            <option> based upon its text
        2. select_item_by_index
            select_by_index Selects an
            <option> based upon the <select>
            element's internal index
            Index starts from 1
        3. select_by_value
            select_by_value selects an <option>
            based upon its value attribute

"""
# select_item_by_visible_text

# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
# lst_box = driver.find_element_by_id("standard_cars")
# select = Select(lst_box)
# select.select_by_visible_text("Audi")

# select_item_by_index

# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
# lst_box = driver.find_element_by_id("standard_cars")
# select = Select(lst_box)
# time.sleep(3)
# select.select_by_index("4")

# select_item_by_value

# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
# lst_box = driver.find_element_by_id("standard_cars")
# select = Select(lst_box)
# time.sleep(3)
# select.select_by_value("merc")

"""
SELECT OPTION
Returns the list of all the options
(each option is a WebElement)
present in the list box.
Each item of the list is an option
element (WebElement).

first_selected_option
Returns the option (WebElement)
which is currently selected in the list
box.

 “deselect_all”
    deselect
        deselect_by_visible_text
        deselect_by_index
        deselect_by_value
"""
# slect option

# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
# lst_box = driver.find_element_by_id("standard_cars")
# select = Select(lst_box)
# all_options = select.options
# for item in all_options:
#     print(item.text)
#     sleep(1)

# selecting the list item one by by

# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
#
# lst_box = driver.find_element_by_id("standard_cars")
# select = Select(lst_box)
# all_options = select.options
#
# for item in all_options:
#     select.select_by_visible_text(item.text)
#     sleep(1)

"""
first_selected_option
Returns the option (WebElement)
which is currently selected in the list
box.
"""

# first_select_option

# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
# lst_box = driver.find_element_by_id("standard_cars")
# select = Select(lst_box)
# select.select_by_visible_text("Audi")
# currently_selected_option = select.first_selected_option.text
# print(currently_selected_option)

"""
selecting multiple items in
multi-select
"""
# Multiple select

# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
# lst_box = driver.find_element_by_id("standard_cars")
# select = Select(lst_box)
# sleep(10)
# select.select_by_visible_text("Audi")
# sleep(2)
# select.select_by_visible_text("Mercedes")
# sleep(2)
# select.select_by_visible_text("Toyota")
# sleep(2)

# All_selected_option

# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
# lst_box = driver.find_element_by_id("standard_cars")
# select = Select(lst_box)
# select.select_by_visible_text("Audi")
# sleep(2)
# select.select_by_visible_text("Mercedes")
# sleep(2)
# select.select_by_visible_text("Toyota")
# sleep(2)
# all_selected_items = select.all_selected_options

# for item in all_selected_items:
#     print(item.text)

"""
IS_ELEMENT
Returns “True”/"False" if the select
element is multiple select.
"""

# IS_ELEMENT
# getting none doubt

# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/demo%20(1).html")
# lst_box = driver.find_element_by_id("standard_cars")
# sleep(10)
# select = Select(lst_box)
# print(select.is_multiple)

"""
SYNCHRONIZATION
One of the main challenges for successful browser automation is to match the pace of
your script execution with the pace of the application.
Selenium provides two different way's to Achieve Synchronization.
    1. Explicit Wait
    2. Implicit Wait

WebDriverWait (Explicit Wait)
visibility_of_element_located
    - visibility_of_element_located checks if the web element is present on the DOM and
      also visible on the webpage. (Both conditions will be checked)
    - "TimeoutException" will be raised if either the element is not loaded onto the DOM or
      the element is not visible on the web page within timeout period.
    - The __call__ method in visibility_of_element_located class returns a
      webelement if the element is found in DOM as well as visible on the webpage,
      otherwise, a boolean False will be returned.
    - If the element is found in the DOM and also visible on webpage, but disabled, No
      exception will be raised by until method.

"""
# waiting till the page loaded completely

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/loading.html")
# wait = WebDriverWait(driver, 11)
# wait.until(expected_conditions.visibility_of_element_located(("name", "fname")))
#
# driver.find_element_by_name("fname").send_keys("Harish Babu")
# driver.find_element_by_name("lname").send_keys("M G")

# WAIT FOR PROGRESS BAR TO COMPLETE 100% IN DEMO

# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/progressbar.html")
# driver.find_element_by_xpath("//button[text()='Click Me']").click()
# wait = WebDriverWait(driver, timeout=30)
# wait.until(expected_conditions.visibility_of_element_located(("xpath", "//div[text()='100%']")))
# print("Done!")

"""
UNTIL
    until method takes a callable as an argument
    A callable can be either a class which has implemented __call__ method or a decorator
    Until method calls the callable repeatedly with time interval of 0.5 seconds (POLL_FREQUENCY)
    between the function calls.
    If the callable returns Boolean True (or the something which evaluates to Boolean True) within
    timeout period, the script execution will continue as normal without any exceptions.
    If the callable does not return Boolean True (or the something which evaluates not to Boolean True)
    within timeout period, until method raises TimeoutException

VISIBILITY_OF_ELEMENT_LOCATED
    one of the short comings of visibility_of_element_located is that it only checks if
    the web element is loaded in the DOM and visible on the webpage, but it does not check if
    the element is enabled or disabled 
    In-order to include this extra functionality, which is to check for enablement of the web element,
    extend the existing class visibility_of_element_located and customize it to add the extra
    functionality to check for enablement.
    Idea here is to re-define __call__ method of parent class in child class using inheritance.
"""

"""_visibility_of_element_located (customized
class, overriding __call__ method of
Parent class in Child class)"""

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/loading.html")
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         # call the parent (visibility_of_element_located) class __call__ method
#         # __call__ method of parent class 'returns a webelement' if the element is
#         # present in the DOM and also visible on the webpage.
#         # if one of the above conditons is not satisfied, the __call__ method
#         # 'returns boolean False'
#         displayed = super().__call__(driver)
#         # Below code checks if the return value of __call__ is of type 'WebElement'
#         # If the return type is WebElement, then check if it is enabled or not
#         if isinstance(displayed, WebElement):
#             # 'is_enabled' method returns a boolean True if the element is enabled
#             # otherwise, 'is_enabled' method returns boolean False
#             return displayed.is_enabled()
#         else:
#             return False

"""
invisibility_of_element_located
    invisibility_of_element_located takes by locator as an argument. It throws
    TimeoutException if the element is visible even after the timeout period that is specified.
    If the web element does not exist on the DOM, NoSuchElementException or
    StaleElementReferenceException is NOT RAISED.
element_to_be_clickable
    element_to_be_clickable takes by locator as an argument. It throws
    ElementNotClickableException if the element to be clicked is either not visible or not
    enabled or missing from the DOM.
"""

"""
IMPLICIT WAIT
    An implicit wait is to tell WebDriver to poll the DOM for a certain amount of time when trying to find an
    element or elements if they are not immediately available
    Implicit wait will not wait for any condition to be achieved on the webelement. It just waits for the
    webelement to load in the HTML or DOM. If the element is not loaded in the DOM within timeout
    period, “NoSuchElementException” exception is raised.
    The default setting is 0, meaning disabled. Once set, the implicit wait is set for the life of the driver or
    browser session.
"""
# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/haris/OneDrive/Desktop/python_class/html-20220308T105145Z-001/html/loading.html")
# driver.maximize_window()
# driver.implicitly_wait(10)  # is_enabled is not checked, just pause the execution
# driver.find_element_by_name("fname").send_keys("Harish Babu")
# driver.find_element_by_name("lname").send_keys("M G")

"""
MOUSE ACTIONS
    move_to_element
    double_click
"""

# move_to_element

# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("https://www.myntra.com")
# driver.maximize_window()
# sleep(1)
# actions = ActionChains(driver)
# profile = driver.find_element_by_xpath("//span[text()='Profile']")
# actions.move_to_element(profile).perform()
# sleep(1)
# driver.find_element_by_xpath("//a[text()='login / Signup']").click()

# double_click
# doubt

# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("https://www.google.co.in/")
# sleep(3)
# actions = ActionChains(driver)
# click_me = driver.find_elements_by_xpath("//a[text()='Gmail']")
# sleep(3)
# actions.double_click(click_me).perform()

"""send_keys pagedown"""
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# sleep(3)
# actions = ActionChains(driver)
# actions.send_keys(Keys.PAGE_DOWN).perform()

"""send_keys  page up"""
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# sleep(3)
# actions = ActionChains(driver)
# actions.send_keys(Keys.PAGE_DOWN).perform()
# actions.send_keys(Keys.PAGE_UP).perform()
# actions.send_keys(Keys.PAGE_DOWN).perform()
# actions.send_keys(Keys.PAGE_UP).perform()
# actions.send_keys(Keys.PAGE_UP).perform()
# actions.send_keys(Keys.PAGE_UP).perform()
# actions.send_keys(Keys.PAGE_UP).perform()
# actions.send_keys(Keys.PAGE_DOWN).perform()
# actions.send_keys(Keys.PAGE_UP).perform()
# actions.send_keys(Keys.PAGE_DOWN).perform()
# actions.send_keys(Keys.PAGE_DOWN).perform()
# actions.send_keys(Keys.PAGE_DOWN).perform()
# actions.send_keys(Keys.PAGE_UP).perform()

"""arrow down"""""
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# sleep(3)
# actions = ActionChains(driver)
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()

"""arrow up"""""
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# sleep(3)
# actions = ActionChains(driver)
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_UP).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_UP).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_UP).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_UP).perform()
# actions.send_keys(Keys.ARROW_UP).perform()
# actions.send_keys(Keys.ARROW_UP).perform()
# actions.send_keys(Keys.ARROW_UP).perform()
# actions.send_keys(Keys.ARROW_UP).perform()

"""send_keys keys.TAB"""
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# sleep(3)
# actions = ActionChains(driver)
# actions.send_keys(Keys.TAB).perform()
# sleep(2)
# actions.send_keys(Keys.TAB).perform()
# sleep(2)


"""send_keys keys.ENTER"""
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# sleep(3)
# actions = ActionChains(driver)
# driver.find_element_by_xpath("//input[@value='Search store']").send_keys("BOOKS")
# actions.send_keys(Keys.ENTER).perform()
# sleep(2)


"""send_keys keys.ESCAPE"""
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# sleep(3)
# actions = ActionChains(driver)
# driver.find_element_by_xpath("//input[@value='Search store']").send_keys("BOOKS")
# actions.send_keys(Keys.ESCAPE).perform()
# actions.send_keys(Keys.ESCAPE).perform()
# actions.send_keys(Keys.ESCAPE).perform()
# actions.send_keys(Keys.ESCAPE).perform()
# actions.send_keys(Keys.ESCAPE).perform()
# actions.send_keys(Keys.ESCAPE).perform()

"""CONTEXT"""
#doubt
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# sleep(3)
# register_link = driver.find_elements_by_xpath("//a[text()='Register']")
# actions = ActionChains(driver)
# actions.context_click(register_link).perform()

"""Drag and Drop"""
#no error but not working google doubt
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome("./chromedriver")
# driver.maximize_window()
# driver.get("https://www.google.com/")
# sleep(3)
# source_element = driver.find_element_by_xpath("//img[@alt='Google']")
# target_element = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
# actions = ActionChains(driver)
# actions.drag_and_drop(source_element, target_element).perform()