# external imports
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
# internal imports
import share
from pages.base_page import BasePage


class WalkInShowersPage(BasePage):
    """
    LOCATORS
    """

    header_get_estimate_button = (By.XPATH, "//header//button[@type='submit']//span[contains(text(), 'Get estimate')]")
    header_zip_code_field = (By.ID, "zipCode")
    header_zip_code_caption = (By.XPATH, "//header//div[@class='zip--caption']")
    header_zip_code_caption_unknown = (
        By.XPATH, "//header//div[@class='zip--caption'][contains(text(), 'Unknown ZIP Code')]")


class EstimateForm(WalkInShowersPage):
    """
    LOCATORS
    """

    next_button = (By.XPATH, "//div[@class='Button--content']/span[contains(text(), 'Next')]")
    title = (By.XPATH, "//div[@id='StepBodyId']//h4")
    orange_block = (By.XPATH, "//div[@id='StepBodyId']//div[contains(@class, 'text-orangeDeep100')]")
    yes_orange_button = (By.XPATH, "//div[@class='Button--content']/span[contains(text(), 'Yes')]")
    no_orange_button = (By.XPATH, "//div[@class='Button--content']/span[contains(text(), 'Yes')]")

    # Why Interested Question

    why_interested_question_answer_ease_of_use = (
        By.XPATH, "//input[@name='why_interested'][@value='1']/parent::div")
    why_interested_question_answer_safer_bathing = (
        By.XPATH, "//input[@name='why_interested'][@value='2']/parent::div")
    why_interested_question_answer_not_sure = (
        By.XPATH, "//input[@name='why_interested'][@value='4']/parent::div")

    # Project Details Question

    project_details_question_answer_tube = (
        By.XPATH, "//input[@name='projectDetails'][@value='1']/parent::div")
    project_details_question_answer_shower = (
        By.XPATH, "//input[@name='projectDetails'][@value='2']/parent::div")
    project_details_question_answer_not_sure = (
        By.XPATH, "//input[@name='projectDetails'][@value='4']/parent::div")

    # Shower Layout Question

    shower_layout_question_answer_1wall = (
        By.XPATH, "//input[@name='showerLayout'][@value='1']/parent::div")
    shower_layout_question_answer_2walls = (
        By.XPATH, "//input[@name='showerLayout'][@value='2']/parent::div")
    shower_layout_question_answer_not_sure = (
        By.XPATH, "//input[@name='showerLayout'][@value='4']/parent::div")

    # Internal Owner Question

    internal_owner_question_answer_yes = (
        By.XPATH, "//input[@name='internalOwner'][@value='1']/parent::div")
    internal_owner_question_answer_no = (
        By.XPATH, "//input[@name='internalOwner'][@value='0']/parent::div")

    # Internal Mobile Home Question

    internal_mobile_home_question_answer_yes = (
        By.XPATH, "//input[@name='internalMobileHome'][@value='1']/parent::div")
    internal_mobile_home_question_answer_no = (
        By.XPATH, "//input[@name='internalMobileHome'][@value='0']/parent::div")

    # Internal Existing Tub Question

    internal_existing_tube_question_answer_yes = (
        By.XPATH, "//input[@name='internalExistingTub'][@value='1']/parent::div")
    internal_existing_tube_question_answer_no = (
        By.XPATH, "//input[@name='internalExistingTub'][@value='0']/parent::div")

    # Internal Insurance Coverage

    internal_insurance_coverage_question_answer_yes = (
        By.XPATH, "//input[@name='internalInsuranceCoverage'][@value='1']/parent::div")
    internal_insurance_coverage_question_answer_no = (
        By.XPATH, "//input[@name='internalInsuranceCoverage'][@value='0']/parent::div")

    # LHSS

    lhss_question_answer_65years = (
        By.XPATH, "//input[@name='lhss'][@value='1']/parent::div")
    lhss_question_answer_veteran = (
        By.XPATH, "//input[@name='lhss'][@value='2']/parent::div")
    lhss_question_answer_none = (
        By.XPATH, "//input[@name='lhss'][@value='3']/parent::div")

    # Fullname and Email

    contacts_fullname = (
        By.XPATH, "//input[@name='fullName']")
    contacts_fullname_caption = (
        By.XPATH, "//div[contains(@class, 'h6 font-weight-medium')][1]")
    contacts_email = (
        By.XPATH, "//input[@name='email']")
    contacts_email_caption = (
        By.XPATH, "//div[contains(@class, 'h6 font-weight-medium')][2]")

    # Phone Number

    contacts_submit_button = (
        By.XPATH, "//div[@class='Button--content']/span[contains(text(), 'Submit my request')]")
    contacts_phone_field = (
        By.XPATH, "//input[@name='phoneNumber']")
    contacts_phone_caption = (
        By.XPATH, "//div[contains(@class, 'h6 font-weight-medium')]")

    # Confirm Phone

    contacts_confirm_phone_field = (
        By.XPATH, "//input[@name='phoneNumber']")
    contacts_phone_correct_button = (
        By.XPATH, "//div[@class='Button--content']/span[contains(text(), 'Phone number is correct')]")
    contacts_phone_edit_button = (
        By.XPATH, "//div[@class='Button--content']/span[contains(text(), 'Edit phone number')]")

    """
    METHODS
    """

    def is_lhss_question_exists(self, selector=lhss_question_answer_none):
        try:
            WebDriverWait(self.driver, share.configuration['driver_wait_in_sec']).until(
                EC.visibility_of_element_located(selector),
                message=f'Can not find {selector}',
            )
            self.driver.find_element(By.XPATH, "//input[@name='lhss'][@value='3']/parent::div")
        except TimeoutException:
            pass  # todo: add a new line to the log file, that incident has happened
        else:
            return True


class ContactsAlreadyInDatabase(WalkInShowersPage):
    """
    LOCATORS
    """

    title = (By.XPATH,
             "//div[@id='StepBodyId']//h4[contains(text(), 'This phone number and email already exist in our database.')]")


class NoMatchingContractors(WalkInShowersPage):
    """
    LOCATORS
    """

    title = (By.XPATH,
             "//div[@id='StepBodyId']//h4[contains(text(), 'Unfortunately, I have no matching contractors in your area yet.')]")
