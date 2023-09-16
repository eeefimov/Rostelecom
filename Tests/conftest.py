import allure
import pytest
from allure_commons._allure import attach
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Pages_Objects.BasePage import BasePage
from Pages_Objects.AuthForm import AuthForm
from Pages_Objects.RecoveryForm import RecoveryForm
from Pages_Objects.RegisterForm import RegisterForm


@pytest.fixture(scope="function")
def browser():
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--user-data-dir=tmp/chrome_profile')
    driver = webdriver.Chrome(service=service, options=options)
    driver.delete_all_cookies()
    driver.set_window_size(1366, 768)

    yield driver

    browser_logs = driver.get_log("browser")
    allure.attach(str(browser_logs), name="Browser Logs", attachment_type=allure.attachment_type.TEXT)

    driver.quit()


@pytest.fixture(scope="function")
def basepage(browser):
    base_page = BasePage(browser)
    return base_page


@pytest.fixture(scope="function")
def authform(browser):
    auth_form = AuthForm(browser)
    return auth_form


@pytest.fixture(scope="function")
def recovery(browser):
    recovery_form = RecoveryForm(browser)
    return recovery_form


@pytest.fixture(scope="function")
def register(browser):
    register_form = RegisterForm(browser)
    return register_form
