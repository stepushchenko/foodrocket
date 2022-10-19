# external imports
from selenium.webdriver.common.by import By
# internal imports
from pages.base_page import Base


class ProductPage(Base):
    add_to_basket = (By.XPATH, "//div[contains(@class, 'addButton')]")
