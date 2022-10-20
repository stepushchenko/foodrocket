# external imports
from selenium.webdriver.common.by import By
# internal imports
from pages.base_page import BasePage


class SearchPage(BasePage):
    title = (By.CLASS_NAME, "src-pages-search-title")
