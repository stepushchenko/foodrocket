# external imports
from selenium.webdriver.common.by import By
# internal imports
from pages.base_page import BasePage


class SignInPage(BasePage):
    phone_field = (By.ID, "Input__phone")
