# external imports
import ipdb
import pytest

# internal imports
from pages.base_page import BasePage
from pages.header_page import HeaderPage
from pages.index_page import IndexPage
from pages.product_page import ProductPage
from pages.sign_in_page import SignInPage


# todo: сделать возможность параметризированного запуска теста (подстановки разных данных в тест)


class TestLogin:

    def test_open_product_page(self, driver, env):
        browser = BasePage(driver, env)
        # ipdb.set_trace()
        browser.open('')
        browser.click(IndexPage.product_card)
        browser.click(ProductPage.add_to_basket)
        browser.enter_value(SignInPage.phone_field, '9003296989')
