import pytest
import allure
from Tests.params import params_auth_form_tabs_name_requirement, params_auth_form_value_auto_tab


@allure.id("RST-6")
@allure.feature("Authorization form")
@allure.suite("Authorization form")
@allure.title("Presence of Authorization form on the base page")
@allure.description_html("""
Confirm the presence of the Authorization form on the base page.
<br><br><b>Expected result</b>:
<br>Authorization form is displayed on the base page.
""")
def test_check_auth_form(authform):
    authform.auth_form_check_auth_form()


@allure.id("RST-7")
@allure.feature("tabs names")
@allure.suite("Authorization form")
@allure.title("Check tabs names on Authorization form")
@allure.description_html("""
Check tabs names on the authorization form are match the requirements.
<br><br><b>Expected result</b>:
<br>All tabs name are match the requirements.
""")
@allure.issue("https://github.com/eeefimov/RostelecomTesting/issues/2#issue-1848254464", "GitHub: In Authentication form Phone Number tab has wrong title")
@pytest.mark.parametrize(("tabs", "tab_name"), params_auth_form_tabs_name_requirement)
def test_auth_form_check_tabs_names(authform, tabs, tab_name):
    authform.auth_form_check_tabs_names(tabs, tab_name)


@allure.id("RST-8")
@allure.feature("Default auth method")
@allure.suite("Authorization form")
@allure.title("Default method Tab")
@allure.description_html("""
Check that authentication by phone tab is selected by default.
<br><br><b>Expected result</b>:
<br>The default tab's name is ‘Телефон’ and the color is ‘rgba(255, 79, 18, 1)’.
""")
def test_auth_form_default_tab(authform):
    authform.auth_form_default_tab()


@allure.id("RST-9")
@allure.feature("Password Field")
@allure.suite("Authorization form")
@allure.title("Presence of Password Field in Auth Forms")
@allure.description_html("""
Check for the presence of a password input field in all authentication selection forms.
<br><br><b>Expected result</b>:
<br>The password field is present in all tabs.
""")
def test_auth_form_tabs_password(authform):
    authform.auth_form_tabs_password()


@allure.id("RST-10")
@allure.feature("Auto Switch Tab")
@allure.suite("Authorization form")
@allure.title("Auto Switch Tab in the Authorization Field (Phone)")
@allure.description_html("""
Verify that the authentication selection tab changes automatically when entering a phone number in 
the authorization field.
<br><br><b>Expected result</b>:
<br>The Phone tab's color and name match the expected values after the tab switch.
""")
@allure.issue("https://github.com/eeefimov/RostelecomTesting/issues/3#issue-1848261849", "GitHub: Tab doesn't switch with to Personal Account ")
@pytest.mark.parametrize(("checks"), params_auth_form_value_auto_tab)
def test_auth_form_tab_phone_auto_switch(authform, checks):
    authform.auth_form_tab_phone_auto_switch(checks)


@allure.id("RST-11")
@allure.feature("Auto Switch Tab")
@allure.suite("Authorization form")
@allure.title("Auto Switch Tab in the Authorization Field (Mail)")
@allure.description_html("""
Verify that the authentication selection tab changes automatically when entering a email in 
the authorization field ().
<br><br><b>Expected result</b>:
<br>The email tab's color and name match the expected values after the tab switch.
""")
@pytest.mark.parametrize(("checks"), params_auth_form_value_auto_tab)
def test_auth_form_tab_mail_auto_switch(authform, checks):
    authform.auth_form_tab_mail_auto_switch(checks)


@allure.id("RST-12")
@allure.feature("Auto Switch Tab")
@allure.suite("Authorization form")
@allure.title("Auto Switch Tab in the Authorization Field (Login)")
@allure.description_html("""
Verify that the authentication selection tab changes automatically when entering a login in 
the authorization field.
<br><br><b>Expected result</b>:
<br>The login tab's color and name match the expected values after the tab switch.
""")
@allure.issue("https://github.com/eeefimov/RostelecomTesting/issues/4#issue-1848273851", "GitHub: Tab doesn't switch with to Phone")
@pytest.mark.parametrize(("checks"), params_auth_form_value_auto_tab)
def test_auth_form_tab_login_auto_switch(authform, checks):
    authform.auth_form_tab_login_auto_switch(checks)


@allure.id("RST-13")
@allure.feature("Auto Switch Tab")
@allure.suite("Authorization form")
@allure.title("Auto Switch Tab in the Authorization Field (Personal account)")
@allure.description_html("""
Verify that the authentication selection tab changes automatically when entering an account number in 
the authorization field.
<br><br><b>Expected result</b>:
<br>Authentication selection tab changes automatically when entering an account number in 
the authorization field.
""")
@allure.issue("https://github.com/eeefimov/RostelecomTesting/issues/5#issue-1848276137", "GitHub: Tab doesn't switch")
@pytest.mark.parametrize(("checks"), params_auth_form_value_auto_tab)
def test_auth_form_tab_personal_account_auto_switch(authform, checks):
    authform.auth_form_tab_personal_account_auto_switch(checks)


@allure.id("RST-14")
@allure.feature("Tabs Labels")
@allure.suite("Authorization form")
@allure.title("Verify Tab's Label Change")
@allure.description_html("""
Ensure that the label in the authorization field changes to match the title of each tab.
<br><br><b>Expected result</b>:
<br>Label for each tab match their respective tab titles.
""")
def test_auth_form_tabs_labels(authform):
    authform.auth_form_tabs_labels()