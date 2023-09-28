import pytest
import allure
from Tests.params import params_auth_form_tabs_name_requirement, params_auth_form_value_auto_tab


@allure.id("RST-15")
@allure.feature("Password recovery form")
@allure.suite("Password recovery form")
@allure.title("Open Password recovery form")
@allure.description("""
Confirm the presence of the Password recovery form after clicking proper link on the base page.

Expected result:
Password recovery form is displayed after clicking proper link on the base page.
""")
def test_recovery_form_check_form(recovery):
    recovery.recovery_form_check_form()


@allure.id("RST-16")
@allure.feature("Tab's name")
@allure.suite("Password recovery form")
@allure.title("Check tabs names on Password recovery form")
@allure.description("""
Check tabs names on the authorization form are match the requirements.

Expected result:
All tabs name are match the requirements.
""")
@pytest.mark.parametrize(("tabs", "tab_name"), params_auth_form_tabs_name_requirement)
def test_recovery_form_tabs_names(recovery, tabs, tab_name):
    recovery.recovery_form_tabs_names(tabs, tab_name)


@allure.id("RST-17")
@allure.feature("Captcha")
@allure.suite("Password recovery form")
@allure.title("Captcha Presence on Password Recovery Form")
@allure.description("""
Check that the 'Captcha' element (image and input field) is present in the password recovery form.

Expected result:
The captcha image and input field should be present on Password Recovery form.
""")
def test_recovery_form_captcha(recovery):
    recovery.recovery_form_captcha()


@allure.id("RST-18")
@allure.feature("Continue Back buttons")
@allure.suite("Password recovery form")
@allure.title("Continue and Back buttons are Presence on Password Recovery Form")
@allure.description("""
Check that the 'Captcha' element (image and input field) is present in the password recovery form.

Expected result:
Continue and Back buttons should be present on Password Recovery form.
""")
def test_restore_form_continue_back_buttons(recovery):
    recovery.recovery_form_continue_back_buttons()


@allure.id("RST-19")
@allure.feature("Continue button's name")
@allure.suite("Password recovery form")
@allure.title("Continue button's name")
@allure.description("""
Check that Continue button's name on Password Recovery Form is match the requirement.

Expected result:
Continue button's name on Password Recovery Form is match the requirement.
""")
def test_recovery_form_continue_button_name(recovery):
    recovery.recovery_form_continue_button_name()


@allure.id("RST-20")
@allure.feature("Return button's name")
@allure.suite("Password recovery form")
@allure.title("Return button's name")
@allure.description("""
Check that Return button's name on Password Recovery Form is match the requirement.

Expected result:
Return button's name on Password Recovery Form is match the requirement.
""")
def test_recovery_form_return_button_name(recovery):
    recovery.recovery_form_return_button_name()


@allure.id("RST-21")
@allure.feature("Return button's function")
@allure.suite("Password recovery form")
@allure.title("Return button's function")
@allure.description("""
Check that after clicking Return button's on Password Recovery Form system should redirect back to Authorization form.

Expected result:
Redirection back to Authorization form after Return button click on Password recovery form.
""")
def test_recovery_form_return_button_function(recovery):
    recovery.recovery_form_return_button_function()


@allure.id("RST-22")
@allure.feature("Default tab")
@allure.suite("Password recovery form")
@allure.title("Phone tab by default")
@allure.description("""
Check that Phone tab is default set on Password Recovery Form.

Expected result:
The default tab should be 'Телефон' (Phone) and have the correct color.
""")
def test_recovery_form_default_tab_phone(recovery):
    recovery.recovery_form_default_tab_phone()


@allure.id("RST-23")
@allure.feature("Error message")
@allure.suite("Password recovery form")
@allure.title("Error message with missing Captcha or wrong data")
@allure.description("""
Verify that an error message appears if the 'Captcha' field is left empty 
when attempting to proceed in the password recovery form. 
This test case checks if an error message is displayed when the 'Captcha' field is empty.

Expected result:
An error message should appear if the 'Captcha' field is left empty
when attempting to proceed in the password recovery form. Or wrong value in the login field.
""")
@pytest.mark.parametrize("values", params_auth_form_value_auto_tab)
def test_recovery_form_continue_btn_error(recovery, values):
    recovery.recovery_form_continue_btn_error(values)


@allure.id("RST-24")
@allure.feature("Error message")
@allure.suite("Password recovery form")
@allure.title("Error message with missing Captcha or empty data")
@allure.description_html("""
Verify that an error message appears if the 'Captcha' field is left empty 
when attempting to proceed in the password recovery form. 
This test case checks if an error message is displayed when login field is empty.

Expected result:
An error message should appear if the 'Captcha' and login field is left empty 
when attempting to proceed in the password recovery form.
""")
def test_recovery_form_continue_btn_error_empty(recovery):
    recovery.recovery_form_continue_btn_error(values="")
