# external imports
import pytest

# internal imports
from pages.base_page import Base
from pages.header_page import HeaderPage
from pages.index_page import IndexPage
from pages.product_page import ProductPage
from pages.sign_in_page import SignInPage


class TestLogin:

    def test_open_product_page(self, driver, env):
        browser = Base(driver, env)
        browser.open('')
        browser.click(IndexPage.product_card)
        browser.click(ProductPage.add_to_basket)
        browser.enter_value(SignInPage.phone_field, '9003296989')
