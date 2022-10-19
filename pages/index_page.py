# external imports
from selenium.webdriver.common.by import By
# internal imports
from pages.base_page import Base


class IndexPage(Base):
    product_card = (By.XPATH, "//a[@class='src-comp-product-productInner']")
