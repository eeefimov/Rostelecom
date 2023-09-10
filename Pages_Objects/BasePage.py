from selenium.webdriver.common.by import By
import allure
import time
from allure_commons.types import AttachmentType
from Pages_Objects.Main import Main


class BasePage(Main):
    def __init__(self, driver):
        super().__init__(driver)

    basepage_left_section = (By.ID, 'page-left')
    basepage_right_section = (By.ID, 'page-right')
    basepage_logo = (By.CLASS_NAME, "what-is-container__logo-container")
    basepage_slogan = (By.CLASS_NAME, "what-is__desc")
    basepage_forgot_password_link = (By.ID, "forgot_password")
    basepage_registration_link = (By.ID, "kc-register")

    def base_page_with_sides(self):
        self.go_to_site()

        with allure.step("Check two vertical blocs split the page"):
            left = self.get_element(self.basepage_left_section)
            right = self.get_element(self.basepage_right_section)
            assert left.is_displayed()
            assert right.is_displayed()

    def base_page_sides_different_window_size(self, width, hight):
        self.go_to_site()

        with allure.step("Check two vertical blocs split the page"):
            left = self.get_element(self.basepage_left_section)
            right = self.get_element(self.basepage_right_section)
            assert left.is_displayed()
            assert right.is_displayed()

        with allure.step("Set window size"):
            self.set_window_size(width, hight)
            time.sleep(5)

        with allure.step("Check two side blocks are displayed"):
            if left.is_displayed() and right.is_displayed():
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="SideBlocks",
                              attachment_type=AttachmentType.PNG)
                assert False

    def base_page_check_logo_slogan(self):
        self.go_to_site()

        with allure.step("Locate and check basepage_slogan is displayed"):
            logo = self.get_element(self.basepage_logo)
            slogan = self.get_element(self.basepage_slogan)
            assert slogan.is_displayed()
            assert logo.is_displayed()

    def base_page_check_links(self, link_name: str, links_locator_name):
        self.go_to_site()

        with allure.step(f"Check '{link_name}' link is presented on the page"):
            link = self.get_element(links_locator_name)
            assert link.is_displayed()

    def base_page_check_register_link(self):
        self.base_page_check_links('registration', self.basepage_registration_link)

    def base_page_check_forgot_link(self):
        self.base_page_check_links('forgot password', self.basepage_forgot_password_link)
