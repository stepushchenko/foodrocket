# external imports
from selenium.webdriver.common.by import By
# internal imports
from pages.base_page import BasePage


class FooterPage(BasePage):
    contact_us_button = (By.XPATH, "//div[@class='src-comp-footer-col']/a[contains(@class, 'intercomLauncher')]")
    app_store_button = (By.XPATH, "//div[@class='src-comp-footer-col']/a[contains(@class, 'src-comp-footer-linkDownload')][1]")
    google_play_button = (By.XPATH, "//div[@class='src-comp-footer-col']/a[contains(@class, 'src-comp-footer-linkDownload')][2]")
