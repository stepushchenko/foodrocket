# external imports
from selenium.webdriver.common.by import By
# internal imports
from pages.base_page import BasePage


class ThankYouPage(BasePage):
    """
    LOCATORS
    """

    title = (By.XPATH, "//div[@id='StepBodyId']//h4[contains(text(), 'Thank you')]")
    subtitle = (By.XPATH, "//div[@id='StepBodyId']//h4/following::div[contains(text(), 'Please')]")

    """
    METHODS
    """

    def is_first_name_present_in_the_title(self, expected_result, title=title):
        title = self.is_element_present(title).text
        actual_result = title.split()
        actual_result = actual_result[2][0:-1]
        assert actual_result == expected_result, f"Actual result: {actual_result}, expected result: {expected_result}"
