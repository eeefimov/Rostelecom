from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import ElementNotVisibleException, NoSuchElementException, TimeoutException
import allure


class Main:
    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru"
        self.driver.implicitly_wait(timeout)

    def go_to_site(self) -> None:
        """
        Opens the main website at the specified base URL.
        """
        with allure.step("Go to site"):
            self.driver.get(self.base_url)
            self.driver.implicitly_wait(5)

    def get_element_name(self, by_locator):
        """
        Gets the text of an element identified by the given locator.
        """
        element = WDW(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def do_element_click(self, by_locator) -> None:
        """
        Performs a click action on an element identified by the given locator.
        """
        WDW(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()

    def element_displayed(self, by_locator):
        """
        Checks if an element identified by the given locator is displayed.
        """
        element = WDW(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return bool(element)

    def get_element(self, by_locator):
        """
        Waits for and returns an element identified by the given locator.
        """
        element = WDW(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def set_window_size(self, width, height):
        """
        Sets the window size of the browser window.
        """
        self.driver.set_window_size(width, height)

    def get_param_element(self, locator_from_params):
        """
        Gets the locator for an element based on the provided parameter.
        """
        self.driver.implicitly_wait(3)
        locator = (By.ID, locator_from_params)
        return locator

    def get_color(self, element):
        """
        Gets the CSS color property of a given element.
        """
        self.driver.implicitly_wait(3)
        tab_element = self.get_element(element)
        current_color = tab_element.value_of_css_property("color")
        return current_color

    def do_element_send_keys(self, by_locator, text_keys) -> None:
        """
        Sends the specified text to an element identified by the given locator.
        """
        WDW(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text_keys)

    def wait_exaption(self):
        """
        Creates and returns a WebDriverWait instance with custom exceptions.
        """
        wait = WDW(self.driver, timeout=2, poll_frequency=1, ignored_exceptions=
        [ElementNotVisibleException, NoSuchElementException, TimeoutException])
        return wait

    def wait_not_element(self, by_locator):
        """
        Waits for an element identified by the given locator to disappear.
        """
        try:
            wait = self.wait_exaption()
            wait.until_not(EC.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False