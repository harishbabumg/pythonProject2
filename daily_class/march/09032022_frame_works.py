from selenium.webdriver import Chrome
from time import sleep
import csv
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color


class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False


def wait(func):
    def wrapper(*args, **kwargs):
        locator = args[0]
        wait = WebDriverWait(driver, 20)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper


@wait
def click_element(locator):
    driver.find_element(*locator).click()


@wait
def enter_text(locator, * , value):
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(value)


@wait
def select_item(locator, *, item):
    element = driver.find_element(*locator)
    s = Select(element)
    if isinstance(item, str):
        s.select_by_visible_text(item)
    elif isinstance(item, int):
        s.select_by_index(item)
    else:
        raise TypeError


driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get('http://demowebshop.tricentis.com/')
sleep(3)

click_element(("link text", "Register"))
click_element(("id", "gender-male"))
enter_text(("name", "FirstName"), value="hello")
enter_text(("name", "LastName"), value="world")
enter_text(("id", "Email"), value="hello.world@company.com")
enter_text(("id", "Password"), value="Password123")
enter_text(("id", "ConfirmPassword"), value="Password123")
click_element(("id", "register-button"))
driver.close


