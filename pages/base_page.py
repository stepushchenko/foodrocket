# external imports
import platform
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# internal imports
import share


class BasePage:
    def __init__(self, driver, env):
        self.driver = driver
        self.frontend_url = env['frontend_url']

    """
    STEPS
    """

    def open(self, url):
        self.driver.get(f"{self.frontend_url}{url}")

    def click(self, selector):
        self.is_element_present(selector).click()

    def enter_value(self, selector, value):
        self.is_element_present(selector).send_keys(value)

    def clear_value(self, selector):
        element = self.is_element_present(selector)
        if platform.system() == 'Darwin':
            element.send_keys(Keys.COMMAND + "a")
            element.send_keys(Keys.DELETE)
        else:
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.DELETE)

    def press_keyboard_numbers(self, value: str):
        action = ActionChains(self.driver)
        for num in value:
            numpad = 'NUMPAD' + num
            action.send_keys(Keys.__str__(numpad))
        action.perform()

    def generate_uniq_email_address(self, domain: str):
        email = str(time.time_ns()) + '@' + domain
        return email

    # def focus(self, element):
    #     self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)  # focus on the element

    """
    ASSERTS
    """

    def is_element_present(self, selector: str):
        element = WebDriverWait(self.driver, share.configuration['driver_wait_in_sec']).until(
            EC.visibility_of_element_located(selector),  # return element, if it exists in the DOM
            message=f'Can not find {selector}',  # if no element, print a message
        )
        return element

    def is_text_present(self, selector: str, expected_result: str):
        actual_result = self.is_element_present(selector).text
        assert actual_result == expected_result, f"Actual result: {actual_result}, expected result: {expected_result}"

    def is_value_present(self, selector: str, expected_result: str):
        actual_result = self.is_element_present(selector).get_attribute('value')
        assert actual_result == expected_result, f"Actual result: {actual_result}, expected result: {expected_result}"

    # def is_href_present(self, selector: str, expected_result: str):
    #     actual_result = self.is_element_present(selector).get_attribute('href')
    #     assert actual_result == expected_result, f"Actual result: {actual_result}, expected result: {expected_result}"

    def is_css_color_present(self, selector: str, expected_result: str):
        actual_result = self.is_element_present(selector).value_of_css_property('color')
        assert actual_result == expected_result, f"Actual result: {actual_result}, expected result: {expected_result}"
