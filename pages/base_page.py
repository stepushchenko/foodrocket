# external imports
import pytest
import platform
from selenium.common import NoSuchElementException, TimeoutException, InvalidArgumentException
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

    #
    # STEPS
    #

    def open(self, url):
        self.driver.get(f"{self.frontend_url}{url}")

    def click(self, selector):
        self.wait_element_visible(selector).click()

    def enter_value(self, selector, value):
        self.wait_element_visible(selector).send_keys(value)

    def clear_value(self, selector):
        element = self.wait_element_visible(selector)
        if platform.system() == 'Darwin':
            element.send_keys(Keys.COMMAND + "a")
            element.send_keys(Keys.DELETE)
        else:
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.DELETE)

    #
    # WAITS
    #

    def wait_element_visible(self, selector):
        element = WebDriverWait(self.driver, share.driver_wait_in_sec).until(
            EC.visibility_of_element_located(selector),  # return element, if it exists in the DOM
            message=f'Can not find {selector}',  # if no element, print a message
        )
        # self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)  # focus on the element
        return element

    #
    # ASSERTS
    #

    def is_element_present(self, selector):
        WebDriverWait(self.driver, share.driver_wait_in_sec).until(
            EC.visibility_of_element_located(selector),  # return element, if it exists in the DOM
            message=f'Can not find {selector}',  # if no element, print a message
        )

    def is_text_present(self, selector, expected_result: str):
        actual_result = self.wait_element_visible(selector).text
        assert actual_result == expected_result, f"Actual result: {actual_result}, expected result: {expected_result}"

    def is_value_present(self, selector, expected_result: str):
        actual_result = self.wait_element_visible(selector).get_attribute('value')
        assert actual_result == expected_result, f"Actual result: {actual_result}, expected result: {expected_result}"
