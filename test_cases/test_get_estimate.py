# external imports
import ipdb
import pytest
# internal imports
import share
from pages.thank_you_page import ThankYouPage
from pages.walk_in_showers_page import (WalkInShowersPage,
                                        EstimateForm,
                                        ContactsAlreadyInDatabase,
                                        NoMatchingContractors)


class TestGetEstimate:
    """
    На странице Walk in showers (лендинг) при введении корректного ZIP Code, который не поддерживается
    нашей компанией, получим переход на страницу с уведомлением, что данная территория не обслуживается компанией.
    В данном тесте мы убедимся, что после введения неподдерживаемого кода система перенаправит
    пользователя на страницу с заголовком "Unfortunately, I have no matching contractors in your area yet."
    """
    def test_unmatched_zip_code(self, driver, env):
        walk_in_showers_page = WalkInShowersPage(driver, env)
        walk_in_showers_page.open('walk-in-showers')
        walk_in_showers_page.enter_value(WalkInShowersPage.header_zip_code_field, share.data['unmatched_zip_code'])
        walk_in_showers_page.click(WalkInShowersPage.header_get_estimate_button)
        no_matching_contractors = NoMatchingContractors(driver, env)
        # Check New Page Opened
        no_matching_contractors.is_element_present(NoMatchingContractors.title)

    """
    На странице Walk in showers (лендинг) при некорректном вводе ZIP Code и нажатии кнопки Get Estimate 
    получаем сообщение оранжевого цвета о некорректном ZIP Code. Если введенное значение удалить, то 
    сообщение о некорректном ZIP Code останется, но цвет станет серым. В данном тесте мы убедимся, что
    при повторном вводе некорректного Zip Code сообщение вновь станет оранжевым.
    """
    def test_unknown_zip_code_caption_change_color(self, driver, env):
        walk_in_showers_page = WalkInShowersPage(driver, env)
        walk_in_showers_page.open('walk-in-showers')
        # Insert Invalid ZIP Code
        walk_in_showers_page.enter_value(WalkInShowersPage.header_zip_code_field, share.data['unknown_zip_code'])
        walk_in_showers_page.click(WalkInShowersPage.header_get_estimate_button)
        walk_in_showers_page.clear_value(WalkInShowersPage.header_zip_code_field)
        # Check Grey Caption Color
        walk_in_showers_page.is_css_color_present(WalkInShowersPage.header_zip_code_caption_unknown,
                                                  share.data['zip_code_caption_color'])
        # Insert Invalid ZIP Code Second Time
        walk_in_showers_page.enter_value(WalkInShowersPage.header_zip_code_field, share.data['unknown_zip_code'])
        walk_in_showers_page.click(WalkInShowersPage.header_get_estimate_button)
        # Check Orange Caption Color
        walk_in_showers_page.is_css_color_present(WalkInShowersPage.header_zip_code_caption_unknown,
                                                  share.data['zip_code_warning_caption_color'])

    """
    В процессе заполнения формы заявки на странице Walk in showers требуется указать корректные имя и фамилия. 
    Корректные имя и фамилия должны состоять как минимум из двух слов, должны быть написаны латиницей и 
    не должны содержать никаких дополнительных символов кроме '-'. В данном тесте мы убедимся, что при 
    некорректном заполнении поля пользователю будет выведено соответствующее сообщение об ошибке. 
    """
    @pytest.mark.parametrize("fullname, caption", share.data['invalid_fullname_caption'])
    def test_fullname_field_caption(self, driver, env, fullname, caption):
        walk_in_showers_page = WalkInShowersPage(driver, env)
        walk_in_showers_page.open('walk-in-showers')
        walk_in_showers_page.enter_value(WalkInShowersPage.header_zip_code_field, share.data['valid_zip_code'])
        walk_in_showers_page.click(WalkInShowersPage.header_get_estimate_button)
        estimate_form_page = EstimateForm(driver, env)
        estimate_form_page.click(EstimateForm.why_interested_question_answer_ease_of_use)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.project_details_question_answer_tube)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.shower_layout_question_answer_1wall)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_owner_question_answer_yes)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_mobile_home_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_existing_tube_question_answer_yes)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_insurance_coverage_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_insurance_coverage_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        if estimate_form_page.is_lhss_question_exists():  # todo: разобраться в причинах флакающего появления вопроса
            estimate_form_page.click(EstimateForm.lhss_question_answer_none)
            estimate_form_page.click(EstimateForm.next_button)
        # Insert Fullname
        estimate_form_page.enter_value(EstimateForm.contacts_fullname, fullname)
        estimate_form_page.click(EstimateForm.next_button)
        # Check First Name
        estimate_form_page.is_text_present(EstimateForm.contacts_fullname_caption, caption)

    """
    В процессе заполнения формы заявки на странице Walk in showers пользователь заполняет поле Fullname,
    после чего на странице Thank you система обращается к нему по First name. В данном тесте мы убедимся, что
    система корректно извлекает из Fullname первую часть и корректно отображает ее на странице Thank you. 
    """
    @pytest.mark.parametrize("fullname, first_name", share.data['first_name_in_fullname'])
    def test_correct_user_name_on_the_thank_you_page(self, driver, env, fullname, first_name):
        walk_in_showers_page = WalkInShowersPage(driver, env)
        walk_in_showers_page.open('walk-in-showers')
        walk_in_showers_page.enter_value(WalkInShowersPage.header_zip_code_field, share.data['valid_zip_code'])
        walk_in_showers_page.click(WalkInShowersPage.header_get_estimate_button)
        estimate_form_page = EstimateForm(driver, env)
        estimate_form_page.click(EstimateForm.why_interested_question_answer_ease_of_use)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.project_details_question_answer_tube)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.shower_layout_question_answer_1wall)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_owner_question_answer_yes)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_mobile_home_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_existing_tube_question_answer_yes)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_insurance_coverage_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_insurance_coverage_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        if estimate_form_page.is_lhss_question_exists():  # todo: разобраться в причинах флакающего появления вопроса
            estimate_form_page.click(EstimateForm.lhss_question_answer_none)
            estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.enter_value(EstimateForm.contacts_fullname, fullname)
        """
        p.s.
        При повторном использовании одного и того же набора Email + Phone система выводит
        сообщение о наличии контакта в базе данных. Появление данного сообщения может быть рассмотрено в 
        соответствующем кейсе, в прочих же случаях на каждый тест генерируем уникальный email.
        """
        estimate_form_page.enter_value(EstimateForm.contacts_email,
                                       estimate_form_page.generate_uniq_email_address(share.data['valid_email_domain']))
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.contacts_phone_field)
        estimate_form_page.press_keyboard_numbers(share.data['valid_phone_number_without_code'])
        estimate_form_page.click(EstimateForm.contacts_submit_button)
        estimate_form_page.click(EstimateForm.contacts_phone_correct_button)
        thank_you_page = ThankYouPage(driver, env)
        thank_you_page.is_first_name_present_in_the_title(first_name)

    """
    При повторном использовании одного и того же набора Email + Phone система выводит
    сообщение о наличии контакта в базе данных. В данном тесте мы создадим две заявки с одинаковым набором
    Email + Phone и убедимся, что откроется страница "This phone number and email already exist in our database." 
    """
    def test_contacts_already_exists_in_database(self, driver, env):
        # Generate Uniq Email for Using Twice
        estimate_form_page = EstimateForm(driver, env)
        email = estimate_form_page.generate_uniq_email_address(share.data['valid_email_domain'])
        # First Order
        walk_in_showers_page = WalkInShowersPage(driver, env)
        walk_in_showers_page.open('walk-in-showers')
        walk_in_showers_page.enter_value(WalkInShowersPage.header_zip_code_field, share.data['valid_zip_code'])
        walk_in_showers_page.click(WalkInShowersPage.header_get_estimate_button)
        estimate_form_page.click(EstimateForm.why_interested_question_answer_ease_of_use)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.project_details_question_answer_tube)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.shower_layout_question_answer_1wall)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_owner_question_answer_yes)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_mobile_home_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_existing_tube_question_answer_yes)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_insurance_coverage_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_insurance_coverage_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        if estimate_form_page.is_lhss_question_exists():  # todo: разобраться в причинах флакающего появления вопроса
            estimate_form_page.click(EstimateForm.lhss_question_answer_none)
            estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.enter_value(EstimateForm.contacts_fullname, share.data['valid_fullname'])
        estimate_form_page.enter_value(EstimateForm.contacts_email, email)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.contacts_phone_field)
        estimate_form_page.press_keyboard_numbers(share.data['valid_phone_number_without_code'])
        estimate_form_page.click(EstimateForm.contacts_submit_button)
        estimate_form_page.click(EstimateForm.contacts_phone_correct_button)
        thank_you_page = ThankYouPage(driver, env)
        thank_you_page.is_element_present(ThankYouPage.subtitle)
        # Second Order
        walk_in_showers_page.open('walk-in-showers')
        walk_in_showers_page.enter_value(WalkInShowersPage.header_zip_code_field, share.data['valid_zip_code'])
        walk_in_showers_page.click(WalkInShowersPage.header_get_estimate_button)
        estimate_form_page.click(EstimateForm.why_interested_question_answer_ease_of_use)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.project_details_question_answer_tube)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.shower_layout_question_answer_1wall)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_owner_question_answer_yes)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_mobile_home_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_existing_tube_question_answer_yes)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_insurance_coverage_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.internal_insurance_coverage_question_answer_no)
        estimate_form_page.click(EstimateForm.next_button)
        if estimate_form_page.is_lhss_question_exists():  # todo: разобраться в причинах флакающего появления вопроса
            estimate_form_page.click(EstimateForm.lhss_question_answer_none)
            estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.enter_value(EstimateForm.contacts_fullname, share.data['valid_fullname'])
        estimate_form_page.enter_value(EstimateForm.contacts_email, email)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.contacts_phone_field)
        estimate_form_page.press_keyboard_numbers(share.data['valid_phone_number_without_code'])
        estimate_form_page.click(EstimateForm.contacts_submit_button)
        contacts_already_in_database = ContactsAlreadyInDatabase(driver, env)
        contacts_already_in_database.is_element_present(ContactsAlreadyInDatabase.title)

    """
    В процессе заполнения заявки пользователь может выбрать вариант ответа, который говорит о потенциальных
    сложностях с исполнением такого заказа нашей компанией. При выборе такого ответа система попросит пользователя 
    подтвердить свой выбор. В данном тесте мы проверим, что на каждый соответствующий вопрос система показывает
    корректный текст предупреждения.
    """
    def test_orange_messages_exists(self, driver, env):
        walk_in_showers_page = WalkInShowersPage(driver, env)
        walk_in_showers_page.open('walk-in-showers')
        walk_in_showers_page.enter_value(WalkInShowersPage.header_zip_code_field, share.data['valid_zip_code'])
        walk_in_showers_page.click(WalkInShowersPage.header_get_estimate_button)
        estimate_form_page = EstimateForm(driver, env)
        estimate_form_page.click(EstimateForm.why_interested_question_answer_ease_of_use)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.project_details_question_answer_tube)
        estimate_form_page.click(EstimateForm.next_button)
        estimate_form_page.click(EstimateForm.shower_layout_question_answer_1wall)
        estimate_form_page.click(EstimateForm.next_button)
        # Check Internal Owner Orange Message
        estimate_form_page.click(EstimateForm.internal_owner_question_answer_no)
        estimate_form_page.is_text_present(EstimateForm.orange_block, share.data['orange_message_for_internal_owner'])
        estimate_form_page.click(EstimateForm.yes_orange_button)
        # Check Internal Mobile Home Orange Message
        estimate_form_page.click(EstimateForm.internal_mobile_home_question_answer_yes)
        estimate_form_page.is_text_present(EstimateForm.orange_block,
                                           share.data['orange_message_for_internal_mobile_home'])
        estimate_form_page.click(EstimateForm.yes_orange_button)
        # Check Internal Existing Tube Orange Message
        estimate_form_page.click(EstimateForm.internal_existing_tube_question_answer_no)
        estimate_form_page.is_text_present(EstimateForm.orange_block,
                                           share.data['orange_message_for_internal_existing_tub'])
        estimate_form_page.click(EstimateForm.yes_orange_button)
        # Check Internal Insurance Coverage Orange Message
        estimate_form_page.click(EstimateForm.internal_insurance_coverage_question_answer_yes)
        estimate_form_page.is_text_present(EstimateForm.orange_block,
                                           share.data['orange_message_for_internal_insurance_coverage'])
        estimate_form_page.click(EstimateForm.yes_orange_button)

