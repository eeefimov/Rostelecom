import pytest
import allure
from Tests.params import params_window_size


@allure.id("RST-1")
@allure.feature("Two Blocks")
@allure.suite("Base Page")
@allure.title("Loading the Base Page Split into Two Blocks")
@allure.description("""
Verify that the base page loads correctly and is vertically divided into two distinct blocks.

Expected result:
Both the left and right sections are displayed on the page.
""")
def test_base_page_with_sides(basepage):
    basepage.base_page_with_sides()


@allure.id("RST-2")
@allure.feature("Two Blocks")
@allure.suite("Base Page")
@allure.title("Loading the Base Page Split into Two Blocks (Different Window Size)")
@allure.description("""
Verify that the base page loads correctly and is vertically divided into two distinct blocks when the browser window is 
resized to different dimensions.

Expected result:
Both side blocks remain displayed after resizing the window.
""")
@pytest.mark.parametrize(("width", "height"), params_window_size)
def test_base_page_sides_different_window_size(basepage, width, height):
    basepage.base_page_sides_different_window_size(width, height)


@allure.id("RST-3")
@allure.feature("logo and slogan")
@allure.suite("Base Page")
@allure.title("Presence of slogan and product logo on the Base page")
@allure.description("""
Confirm the presence of the product logo and slogan on the base page.

Expected result:
Both the product logo and slogan are displayed on the base page.
""")
def test_base_page_check_logo_slogan(basepage):
    basepage.base_page_check_logo_slogan()


@allure.id("RST-4")
@allure.feature("Registration link")
@allure.suite("Base Page")
@allure.title("Presence of 'Registration' link on the base page")
@allure.description("""
Confirm the presence of the 'registration' link on the base page.

Expected result:
Registration link is displayed on the base page.
""")
def test_base_page_check_register_link(basepage):
    basepage.base_page_check_register_link()


@allure.id("RST-5")
@allure.feature("Registration link")
@allure.suite("Base Page")
@allure.title("Presence of 'Forgot password' link on the base page")
@allure.description("""
Confirm the presence of the 'forgot password' link on the base page.

Expected result:
Forgot password link is displayed on the base page.
""")
def test_base_page_check_forgot_link(basepage):
    basepage.base_page_check_forgot_link()
