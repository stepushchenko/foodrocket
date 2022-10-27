# external imports
import ipdb
import pytest

# internal imports
from pages.base_page import BasePage
from pages.header_page import HeaderPage
from pages.sign_in_page import SignInPage


class TestLogin:

    def test_phone_number_can_be_entered(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.click(HeaderPage.sign_in_button)
        browser.enter_value(SignInPage.phone_field, '9003296989')
        browser.clear_value(SignInPage.phone_field)
        browser.is_value_present(SignInPage.phone_field, '')

    def test_phone_number_can_be_entered_from_keyboard(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.click(HeaderPage.sign_in_button)
        browser.clear_value(SignInPage.phone_field)
        browser.click(SignInPage.phone_field)
        browser.press_keyboard_numbers('9003296989')
        browser.is_value_present(SignInPage.phone_field, '9003296989')
