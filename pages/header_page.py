# external imports
from selenium.webdriver.common.by import By
# internal imports
from pages.base_page import BasePage


class HeaderPage(BasePage):
    search_field = (By.XPATH, "//div[contains(@class, 'src-comp-mainHeader-searchDesktopWrapper')]")
    search_input = (By.ID, "Input__search")
    search_submit_button = (By.XPATH, "//div[contains(@class, 'src-comp-mainHeader-submit')]")
    sign_in_button = (By.XPATH, "//div[contains(@class, 'src-comp-mainHeader-loginButton')]")






