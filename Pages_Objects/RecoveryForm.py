from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType
from Pages_Objects.AuthForm import AuthForm


class RecoveryForm(AuthForm):
    def __init__(self, driver):
        super().__init__(driver)

    recovery_form_form = (By.CLASS_NAME, "reset-form-container")

    recovery_form_username_field = (By.CSS_SELECTOR, "#username")
    recovery_form_login_field = (By.CSS_SELECTOR, "#username")
    recovery_form_continue_button = (By.CSS_SELECTOR, "#reset")
    recovery_form_return_back_button = (By.CSS_SELECTOR, "#reset-back")

    recovery_form_empty_error = (By.CLASS_NAME, "rt-input-container__meta--error")
    recovery_form_error_error = (By.XPATH, "//span[@id='form-error-message']")

    recovery_form_captcha_img = (By.CSS_SELECTOR, "img.rt-captcha__image")
    recovery_form_captcha_input = (By.CSS_SELECTOR, "input#captcha")

    def recovery_form_go_to_form(self):
        self.go_to_site()

        with allure.step("Click 'Forgot password' link in auth form"):
            self.do_element_click(self.basepage_forgot_password_link)

    def recovery_form_check_form(self):
        self.recovery_form_go_to_form()

        with allure.step("Check Recovery form is displayed"):
            assert self.element_displayed(self.recovery_form_form)

    def recovery_form_tabs_names(self, tabs, tab_name):
        self.recovery_form_go_to_form()

        with allure.step("Find tab in Recovery form"):
            element = self.get_element(self.get_param_element(tabs))

        with allure.step("Check tab's name"):
            tab_element = self.get_element_name(self.get_param_element(tabs))
            if element.is_displayed() and tab_element == tab_name:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Tab's name",
                              attachment_type=AttachmentType.PNG)
                assert False

    def recovery_form_captcha(self):
        self.recovery_form_go_to_form()

        with allure.step("Check captcha image and field are displayed"):
            assert self.element_displayed(self.recovery_form_captcha_img)
            assert self.element_displayed(self.recovery_form_captcha_input)

    def check_button(self, button_element, expected_button_name):
        self.recovery_form_go_to_form()

        with allure.step(f"Check that '{expected_button_name}' button is displayed"):
            assert self.element_displayed(button_element)

        with allure.step("Check button name"):
            actual_button_name = self.get_element_name(button_element)
            if actual_button_name == expected_button_name:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Btn name",
                              attachment_type=AttachmentType.PNG)
                assert False, f"Expected button name: '{expected_button_name}', Actual button name: '{actual_button_name}'"

    def recovery_form_continue_back_buttons(self):
        self.check_button(self.recovery_form_continue_button, 'Продолжить')
        self.check_button(self.recovery_form_return_back_button, 'Вернуться назад')

    def recovery_form_continue_button_name(self):
        self.check_button(self.recovery_form_continue_button, 'Далее')

    def recovery_form_return_button_name(self):
        self.check_button(self.recovery_form_return_back_button, 'Вернуться назад')

    def recovery_form_return_button_function(self):
        self.recovery_form_go_to_form()

        with allure.step("Click 'Return back' button"):
            self.do_element_click(self.recovery_form_return_back_button)

        with allure.step("Check form change back to Authorization form "):
            assert self.element_displayed(self.auth_form_body)

    def recovery_form_default_tab_phone(self):
        self.recovery_form_go_to_form()

        with allure.step("Check tab's name and color"):
            color = self.get_color(self.phone_tab)
            element = self.get_element_name(self.phone_tab)
            assert element == "Телефон" and color == "rgba(255, 79, 18, 1)"

    def recovery_form_continue_btn_error(self, values):
        self.recovery_form_go_to_form()

        if values != "":
            with allure.step("Set value to login field in Recovery form"):
                self.do_element_send_keys(self.recovery_form_username_field, values[0])
        elif values == "":
            with allure.step("Set value to login field in Recovery form"):
                self.do_element_send_keys(self.recovery_form_username_field, "")

        with allure.step("Click 'Continue' button"):
            self.do_element_click(self.recovery_form_continue_button)

        with allure.step("Check error message is displayed"):
            if values == "":
                er = self.get_element(self.recovery_form_empty_error)
            else:
                er = self.get_element(self.recovery_form_error_error)
            assert er.is_displayed()
