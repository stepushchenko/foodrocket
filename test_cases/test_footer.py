# external imports
import ipdb
import pytest

import share
# internal imports
from pages.base_page import BasePage
from pages.footer_page import FooterPage


class TestFooter:

    @pytest.mark.debugging
    def test_link_to_contact_us_button(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.is_href_present(FooterPage.contact_us_button, share.data['contact_us_email'])

    def test_link_to_app_store_button(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.is_href_present(FooterPage.app_store_button, share.data['app_store_download_link'])

    def test_link_to_google_play_button(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.is_href_present(FooterPage.google_play_button, share.data['google_play_market_download_link'])

