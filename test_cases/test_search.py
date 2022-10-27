# external imports
import ipdb
import pytest

# internal imports
import share
from pages.base_page import BasePage
from pages.header_page import HeaderPage
from pages.search_page import SearchPage


class TestSearch:

    def test_search_field_can_be_pressed(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.click(HeaderPage.search_field)
        browser.is_element_present(HeaderPage.search_submit_button)

    def test_search_results_can_be_displayed(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.click(HeaderPage.search_field)
        browser.enter_value(HeaderPage.search_input, share.data['search_titles'][0])
        browser.click(HeaderPage.search_submit_button)
        browser.is_text_present(SearchPage.title, f"Search results for “{share.data['search_titles'][0]}”")
