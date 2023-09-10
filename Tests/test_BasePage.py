import pytest
import allure
from Tests.params import params_window_size


@allure.id("RST-1")
@allure.feature("Two Blocks")
@allure.suite("Base Page")
@allure.title("Loading the Base Page Split into Two Blocks")
@allure.description_html("""
Verify that the base page loads correctly and is vertically divided into two distinct blocks.
<br><br><b>Expected result</b>:
<br>Both the left and right sections are displayed on the page.
""")
def test_base_page_with_sides(basepage):
    basepage.base_page_with_sides()


@allure.id("RST-2")
@allure.feature("Two Blocks")
@allure.suite("Base Page")
@allure.title("Loading the Base Page Split into Two Blocks (Different Window Size)")
@allure.description_html("""
Verify that the base page loads correctly and is vertically divided into two distinct blocks when the browser window is 
resized to different dimensions.
<br><br><b>Expected result</b>:
<br>Both side blocks remain displayed after resizing the window.
""")
@allure.issue("https://github.com/eeefimov/RostelecomTesting/issues/1#issue-1848248873", "Gitlab")
@pytest.mark.parametrize(("width", "hight"), params_window_size)
def test_base_page_sides_different_window_size(basepage, width, hight):
    basepage.base_page_sides_different_window_size(width, hight)


@allure.id("RST-3")
@allure.feature("logo and slogan")
@allure.suite("Base Page")
@allure.title("Presence of slogan and product logo on the Base page")
@allure.description_html("""
Confirm the presence of the product logo and slogan on the base page.
<br><br><b>Expected result</b>:
<br>Both the product logo and slogan are displayed on the base page.
""")
def test_base_page_check_logo_slogan(basepage):
    basepage.base_page_check_logo_slogan()


@allure.id("RST-4")
@allure.feature("Registration link")
@allure.suite("Base Page")
@allure.title("Presence of 'Registration' link on the base page")
@allure.description_html("""
Confirm the presence of the 'registration' link on the base page.
<br><br><b>Expected result</b>:
<br>Registration link is displayed on the base page.
""")
def test_base_page_check_register_link(basepage):
    basepage.base_page_check_register_link()


@allure.id("RST-5")
@allure.feature("Registration link")
@allure.suite("Base Page")
@allure.title("Presence of 'Forgot password' link on the base page")
@allure.description_html("""
Confirm the presence of the 'forgot password' link on the base page.
<br><br><b>Expected result</b>:
<br>Forgot password link is displayed on the base page.
""")
def test_base_page_check_forgot_link(basepage):
    basepage.base_page_check_forgot_link()
