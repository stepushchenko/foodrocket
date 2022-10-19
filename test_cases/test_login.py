# external imports
import time

import pytest
from selenium.webdriver.common.by import By

# internal imports
from pages.base_page import Base
from pages.header_page import HeaderPage
from pages.index_page import IndexPage
from pages.product_page import ProductPage
from pages.sign_in_page import SignInPage


class TestLogin:

    def test_open_product_page(self, driver):
        browser = Base(driver)
        browser.open('https://www.foodrocket.me/')
        browser.click(IndexPage.product_card)
        browser.click(ProductPage.add_to_basket)
        browser.enter_value(SignInPage.phone_field, '9003296989')
