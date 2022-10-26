# external imports
import ipdb
import pytest
from selenium.webdriver.common.by import By

# internal imports
from pages.base_page import BasePage
from pages.header_page import HeaderPage
from pages.index_page import IndexPage
from pages.product_page import ProductPage
from pages.sign_in_page import SignInPage


class TestProduct:

    def test_product_page_can_be_opened(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.click(IndexPage.product_card)
        browser.is_element_present(ProductPage.price_block)
