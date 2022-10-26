# external imports
import ipdb
import pytest

# internal imports
from pages.base_page import BasePage
from pages.header_page import HeaderPage
from pages.index_page import IndexPage
from pages.product_page import ProductPage
from pages.sign_in_page import SignInPage


class TestLogin:

    def test_sign_in_button_can_be_pressed(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.click(HeaderPage.sign_in_button)
        browser.is_element_present(SignInPage.phone_field)
