# external imports
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# internal imports
import share


class BasePage:
    def __init__(self, driver, env):
        self.driver = driver
        self.frontend_url = env['frontend_url']

    def open(self, url):
        self.driver.get(f"{self.frontend_url}{url}")

    def click(self, selector):
        self.wait_element_located(selector).click()

    def enter_value(self, selector, value):
        self.wait_element_located(selector).send_keys(value)

    def wait_element_located(self, selector):
        element = WebDriverWait(self.driver, share.driver_wait_in_sec).until(
            EC.presence_of_element_located(selector),  # return element, if it exists in the DOM
            message=f'Can not find {selector}',  # if no element, print a message
        )
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)  # focus on the element
        return element

    def is_element_present(self, selector):
        try:
            self.driver.find_element(*selector)
        except NoSuchElementException:
            assert False, f"Can not find {selector}"

    def is_text_present(self, selector, text: str):
        result = WebDriverWait(self.driver, share.driver_wait_in_sec).until(
            EC.text_to_be_present_in_element(selector, text),  # return true, if text presents
            message=f"Can not find '{text}' in {selector}"  # if no text, print a message
        )
