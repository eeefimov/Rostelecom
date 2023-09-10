from selenium.webdriver.common.by import By
from Pages_Objects.BasePage import BasePage
from Pages_Objects.RegisterConfirmForm import RConfirmForm
import allure
import string
import time
from allure_commons.types import AttachmentType
from Tests.params import randomize_cyrillic_string, randomize_string


class RegisterForm(BasePage, RConfirmForm):
    def __init__(self, driver):
        super().__init__(driver)

    register_form_form = (By.XPATH, "//h1[contains(text(),'Регистрация')]")

    register_form_name_field = (By.NAME, "firstName")
    register_form_lastname_field = (By.NAME, "lastName")
    register_form_phone_mail_field = (By.CSS_SELECTOR, "#address")
    register_form_pass_field = (By.CSS_SELECTOR, "#password")
    register_form_pass_confirm_field = (By.CSS_SELECTOR, "#password-confirm")

    register_form_registration_button = (By.CLASS_NAME, "register-form__reg-btn")

    register_form_user_agreement_link = (By.LINK_TEXT, "пользовательского соглашения")
    register_form_user_agreement_title = (By.XPATH, "//h1[contains(text(),'Пользователь')]")


    register_form_name_error = (By.CSS_SELECTOR, "div.name-container:nth-child(2) div.rt-input-container.rt-input-container--error:nth-child(1) > span.rt-input-container__meta.rt-input-container__meta--error")
    register_form_lastname_error = (By.CSS_SELECTOR, "div.name-container:nth-child(2) div.rt-input-container.rt-input-container--error:nth-child(2) > span.rt-input-container__meta.rt-input-container__meta--error")
    register_form_phone_mail_field_error = (By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")
    register_form_pass_error = (By.CSS_SELECTOR, "div.rt-input-container.rt-input-container--error.new-password-container__password:nth-child(1) > span.rt-input-container__meta.rt-input-container__meta--error")
    register_form_pass_confirm_error = (By.CSS_SELECTOR, "div.rt-input-container.rt-input-container--error.new-password-container__confirmed-password:nth-child(2) > span.rt-input-container__meta.rt-input-container__meta--error")

    def register_form_go_to_form(self):
        self.go_to_site()

        with allure.step("Click 'Registration' link down the Auth form on the main page"):
            self.do_element_click(self.basepage_registration_link)

        assert self.element_displayed(self.register_form_form)

    def register_form_check_elements(self):
        self.register_form_go_to_form()

        with allure.step("Check all required elements are displayed"):
            assert self.element_displayed(self.register_form_name_field)
            assert self.element_displayed(self.register_form_lastname_field)
            assert self.element_displayed(self.register_form_phone_mail_field)
            assert self.element_displayed(self.register_form_pass_field)
            assert self.element_displayed(self.register_form_pass_confirm_field)
            assert self.element_displayed(self.register_form_registration_button)

    def register_form_registration_btn_name(self):
        self.register_form_go_to_form()

        with allure.step("Check 'Continue' button name"):
            name = self.get_element_name(self.register_form_registration_button)
            if name == "Продолжить":
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Registration btn",
                              attachment_type=AttachmentType.PNG)
                assert False

    def register_form_user_agreement(self):

        self.register_form_go_to_form()

        with allure.step("Click 'User agreement' link"):
            self.do_element_click(self.register_form_user_agreement_link)

        with allure.step("Check redirection to the page with 'User agreement' offer"):
            self.driver.get("https://b2c.passport.rt.ru/sso-static/agreement/agreement.html")
            assert self.element_displayed(self.register_form_user_agreement_title)

    def register_form_check_field(self, select_field, field_name: str, values, expectation, field_error):
        self.register_form_go_to_form()

        with allure.step(f"Click and Set value to '{field_name}' field"):
            self.do_element_click(select_field)
            self.do_element_send_keys(select_field, values)

        with allure.step("Click 'Registration' button"):
            self.do_element_click(self.register_form_registration_button)

        with allure.step(f"Check an error message under '{field_name}' field"):
            error = self.wait_not_element(field_error)

        if error == expectation:
            assert True
        else:
            assert False

    def register_form_check_name_field(self, values, expectation):
        self.register_form_check_field(self.register_form_name_field, "Name", values, expectation,
                                       self.register_form_name_error)

    def register_form_check_lastname_field(self, values, expectation):
        self.register_form_check_field(self.register_form_lastname_field, "Name", values, expectation,
                                       self.register_form_lastname_error)

    def register_form_check_email_field(self, values, expectation):
        self.register_form_check_field(self.register_form_phone_mail_field, "Name", values, expectation,
                                       self.register_form_phone_mail_field_error)

    def register_form_check_phone_field(self, values, expectation):
        self.register_form_check_field(self.register_form_phone_mail_field, "Name", values, expectation,
                                       self.register_form_phone_mail_field_error)

    def register_form_check_password_field(self, values, expectation):
        self.register_form_check_field(self.register_form_pass_field, "Name", values, expectation,
                                       self.register_form_pass_error)

    def register_form_check_confirm_password(self, value1, value2, expectation):
        self.register_form_go_to_form()

        with allure.step("Click and Set value to 'password' field"):
            self.do_element_click(self.register_form_pass_field)
            self.do_element_send_keys(self.register_form_pass_field, value1)

        with allure.step("Click and Set value to 'confirm password' field"):
            self.do_element_click(self.register_form_pass_confirm_field)
            self.do_element_send_keys(self.register_form_pass_confirm_field, value2)

        with allure.step("Click 'Registration' button"):
            self.do_element_click(self.register_form_registration_button)

        with allure.step("Check an error message under 'password' field"):
            assert self.wait_not_element(self.register_form_pass_confirm_error) == expectation

    def register_form_fill_fields(self):
        with allure.step("Click and Set value to 'name' field"):
            self.do_element_click(self.register_form_name_field)
            self.do_element_send_keys(self.register_form_name_field, randomize_cyrillic_string(5))

        with allure.step("Click and Set value to 'lastname' field"):
            self.do_element_click(self.register_form_lastname_field)
            self.do_element_send_keys(self.register_form_lastname_field, randomize_cyrillic_string(5))

        with allure.step("Click and Set value to 'phone or email' field (email)"):
            self.do_element_click(self.register_form_phone_mail_field)
            self.do_element_send_keys(self.register_form_phone_mail_field,
                                      f"{randomize_string(string.ascii_letters, 5)}@maildrop.cc")

        with allure.step("Click and Set value to 'password' field"):
            self.do_element_click(self.register_form_pass_field)
            self.do_element_send_keys(self.register_form_pass_field, "1234!@#$QWERasdf")

        with allure.step("Click and Set value to 'confirm password' field"):
            self.do_element_click(self.register_form_pass_confirm_field)
            self.do_element_send_keys(self.register_form_pass_confirm_field, "1234!@#$QWERasdf")

        field = self.get_element(self.register_form_phone_mail_field)
        user_email = field.get_attribute("value")

        with allure.step("Click 'Registration' button"):
            self.do_element_click(self.register_form_registration_button)

        return user_email


    def register_form_confirm_check_code_elements(self):
        self.register_form_go_to_form()
        self.register_form_fill_fields()
        with allure.step("Check: "
                         "Redirection to 'code confirm by email' form"
                         "Check code fields is displayed"
                         "Check 'Change email' link"
                         ):
            assert self.element_displayed(RConfirmForm.r_confirm_form)
            assert self.element_displayed(RConfirmForm.r_confirm_codemail_code_field)
            assert self.element_displayed(RConfirmForm.r_confirm_codemail_change_mail_link)

    def register_form_confirm_check_repeat_btn(self):
        self.register_form_go_to_form()
        self.register_form_fill_fields()
        with allure.step("Wait 121 sec then Check: 'Repeat code' button is displayed"):
            time.sleep(121)
            assert self.element_displayed(RConfirmForm.r_confirm_codemail_repeat_code_btn)

    def register_form_confirm_change_email(self):
        self.register_form_go_to_form()
        self.register_form_fill_fields()

        with allure.step("Click 'Change email' btn"):
            self.do_element_click(RConfirmForm.r_confirm_codemail_change_mail_link)

        with allure.step("Check rediraction to 'Register' form and user data"):
            assert self.element_displayed(self.register_form_form)

    def register_form_confirm_wrong_code_error(self):
        self.register_form_go_to_form()
        self.register_form_fill_fields()

        with allure.step("Set up wrong number to code fields"):
            self.do_element_send_keys(RConfirmForm.r_confirm_codemail_code_field, 123456)
            time.sleep(2)
            assert self.element_displayed(RConfirmForm.r_confirm_codemail_error_wrong_code)

    def register_form_confirm_mail_masked(self):
        self.register_form_go_to_form()
        user_email = self.register_form_fill_fields()

        with allure.step("Check user mail is masked"):
            assert self.element_displayed(RConfirmForm.r_confirm_codemail_hide_mail)
            masked_mail = self.get_element_name(RConfirmForm.r_confirm_codemail_hide_mail)
            found = user_email in masked_mail

            if found == False:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Masked mail",
                              attachment_type=AttachmentType.PNG)
                assert False








