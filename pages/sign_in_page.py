# external imports
from selenium.webdriver.common.by import By
# internal imports
from pages.base_page import Base


class SignInPage(Base):
    phone_field = (By.XPATH, "//input[@id='Input__phone']")
