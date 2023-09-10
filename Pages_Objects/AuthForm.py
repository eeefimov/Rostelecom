from selenium.webdriver.common.by import By
import allure
import pytest
from allure_commons.types import AttachmentType
import time
from Pages_Objects.BasePage import BasePage


class AuthForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    auth_form_body = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
    auth_form_field_id = (By.ID, 'username')
    auth_form_field_pass = (By.ID, 'password')

    auth_form_phone_label = (By.XPATH, "//span[contains(text(),'Мобильный телефон')]")
    auth_form_mail_label = (By.XPATH, "//span[contains(text(),'Электронная почта')]")
    auth_form_login_label = (By.XPATH, "//span[contains(text(),'Логин')]")
    auth_form_ls_label = (By.XPATH, "//span[contains(text(),'Лицевой счёт')]")

    phone_tab = (By.ID, "t-btn-tab-phone")
    mail_tab = (By.ID, "t-btn-tab-mail")
    login_tab = (By.ID, "t-btn-tab-login")
    ls_tab = (By.ID, "t-btn-tab-ls")

    def auth_form_check_auth_form(self):
        self.go_to_site()
        assert self.element_displayed(self.auth_form_body)

    def auth_form_check_tabs_names(self, tabs, tab_name):
        self.go_to_site()

        with allure.step("Find tab in Auth form"):
            element = self.get_element(self.get_param_element(tabs))

        with allure.step("Check tab's name"):
            tab_element = self.get_element_name(self.get_param_element(tabs))
            assert element.is_displayed()
            if tab_element == tab_name:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="TabNames",
                              attachment_type=AttachmentType.PNG)
                assert False

    def auth_form_default_tab(self):
        self.go_to_site()

        with allure.step("Check tab's name and color"):
            color = self.get_color(self.phone_tab)
            element = self.get_element_name(self.phone_tab)
            assert element == "Телефон" and color == "rgba(255, 79, 18, 1)"

    def auth_form_tabs_password(self):
        self.go_to_site()

        with allure.step("Check password field in default tab"):
            assert self.element_displayed(self.auth_form_field_pass)

        with allure.step("Click next tab, Check password field"):
            self.do_element_click(self.mail_tab)
            assert self.element_displayed(self.mail_tab)

        with allure.step("Click next tab, Check password field"):
            self.do_element_click(self.login_tab)
            assert self.element_displayed(self.login_tab)

        with allure.step("Click next tab, Check password field"):
            self.do_element_click(self.ls_tab)
            assert self.element_displayed(self.ls_tab)

    def tab_auto_switch(self, checks, tabs_name, tab):
        self.go_to_site()

        with allure.step(f"Click {tabs_name} tab"):
            self.do_element_click(tab)

        with allure.step("Click Login field"):
            self.do_element_click(self.auth_form_field_id)

        with allure.step("Set value to Login field"):
            self.do_element_send_keys(self.auth_form_field_id, checks[0])

        with allure.step("Click Pass field"):
            time.sleep(2)
            self.do_element_click(self.auth_form_field_pass)

        with allure.step("Check tab switch (verify tab: color, name)"):
            color = self.get_color(self.get_param_element(checks[2]))
            name = self.get_element_name(self.get_param_element(checks[2]))
            if color == "rgba(255, 79, 18, 1)" and name == checks[1]:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name=f"AutoSwitch_{checks[2]}",
                              attachment_type=AttachmentType.PNG)
                assert False

        with allure.step(f"Click {tab} tab"):
            self.do_element_click(tab)

    def auth_form_tab_phone_auto_switch(self, checks):
        self.tab_auto_switch(checks, "Phone", self.phone_tab)

    def auth_form_tab_mail_auto_switch(self, checks):
        self.tab_auto_switch (checks, "Email", self.mail_tab)

    def auth_form_tab_login_auto_switch(self, checks):
        self.tab_auto_switch (checks, "Login", self.login_tab)

    def auth_form_tab_personal_account_auto_switch(self, checks):
        self.tab_auto_switch (checks, "Personal Account", self.ls_tab)

    def tabs_and_labels_names(self, tab, label, tab_name_str : str, label_name_str : str):
        tab_name = self.get_element_name(tab)
        label_name = self.get_element_name(label)
        assert tab_name == tab_name_str and label_name == label_name_str

    def auth_form_tabs_labels(self):
        self.go_to_site()

        with allure.step ("Check Login field label with Phone tab"):
            self.tabs_and_labels_names(self.phone_tab, self.auth_form_phone_label, "Телефон", "Мобильный телефон")

        with allure.step("Click next tab, Check password field"):
            self.do_element_click(self.mail_tab)

        with allure.step("Check Login field label with Mail tab"):
            self.tabs_and_labels_names(self.mail_tab, self.auth_form_mail_label, "Почта", "Электронная почта")

        with allure.step("Click next tab, Check password field"):
            self.do_element_click(self.login_tab)

        with allure.step("Check Login field label with Login tab"):
            self.tabs_and_labels_names(self.login_tab, self.auth_form_login_label, "Логин", "Логин")

        with allure.step("Click next tab, Check password field"):
            self.do_element_click(self.ls_tab)

        with allure.step("Check Login field label with Personal account tab"):
            self.tabs_and_labels_names(self.ls_tab, self.auth_form_ls_label, "Лицевой счёт", "Лицевой счёт")
