# external imports
import ipdb
import pytest

# internal imports
from pages.base_page import BasePage
from pages.footer_page import FooterPage


@pytest.mark.debugging
class TestFooter:

    def test_link_to_contact_us_button(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.is_href_present(FooterPage.contact_us_button, "mailto:support@foodrocket.me")

    def test_link_to_app_store_button(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.is_href_present(FooterPage.app_store_button, "https://apps.apple.com/app/food-rocket-grocery-delivery/id1552202489")

    def test_link_to_google_play_button(self, driver, env):
        browser = BasePage(driver, env)
        browser.open('')
        browser.is_href_present(FooterPage.google_play_button, "https://play.google.com/store/apps/details?id=me.foodrocket.app")

