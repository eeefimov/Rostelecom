import pytest
import allure
from Tests.params import params_register_values_name_lastname, params_register_values_email, \
    params_register_values_phone, params_register_values_password, params_register_values_password_confirmed


@allure.id("RST-25")
@allure.feature("Registration Form")
@allure.suite("Register Form")
@allure.title("Open Registration Form")
@allure.description_html("""
Check that the Registration Form is displayed on the page.
<br><br><b>Expected result</b>:
<br>The registration form should be displayed on the page.
""")
def test_register_form_go_to_form(register):
    register.register_form_go_to_form()


@allure.id("RST-26")
@allure.feature("Form elements")
@allure.suite("Register Form")
@allure.title("Elements Presence on Register Form")
@allure.description_html("""
Verify that all elements specified in the documentation are present in the Registration form.
<br><br><b>Expected result</b>:
<br>All specified UI elements should be displayed on the registration form.
""")
def test_register_form_check_elements(register):
    register.register_form_check_elements()


@allure.id("RST-27")
@allure.feature("Next Button Name")
@allure.suite("Register Form")
@allure.title("Next Button Name Validation")
@allure.description_html("""
Validate that the name of the button for proceeding in the registration form matches the documentation.
<br><br><b>Expected result</b>:
<br>The name of the button for proceeding should match the documentation (e.g., 'Продолжить').
""")
@allure.issue("https://github.com/eeefimov/RostelecomTesting/issues/7#issue-1848297309",
              "GitHub: In Register form wrong proceeding button name")
def test_register_form_registration_btn_name(register):
    register.register_form_registration_btn_name()


@allure.id("RST-28")
@allure.feature("User agreement")
@allure.suite("Register Form")
@allure.description_html("""
Verify that clicking on the 'User Agreement' link in the registration form redirects to the User Agreement page.
<br><br><b>Expected result</b>:
<br>The browser should redirect to the User Agreement page upon clicking the link.
""")
def test_register_form_user_agreement(register):
    register.register_form_user_agreement()


@allure.id("RST-29")
@allure.feature("Name Field")
@allure.suite("Register Form")
@allure.title("User Registration form Name Field Validation")
@allure.description_html("""
Validate the 'Name' field in the User Registration form with various input substitutions. 
According to the documentation, the field should accept a range of 2 to 30 characters. 
The input field must contain at least 2 characters consisting of Cyrillic letters or a hyphen (-).
The system should verify the field and display an error if it does not meet the requirements.
<br><br><b>Expected result</b>:
<ul>
    <li>For valid names (2 to 30 characters consisting of Cyrillic letters or a hyphen), no error message should be displayed.</li>
    <li>For invalid names (less than 2 characters, more than 30 characters, or containing characters other than Cyrillic letters and hyphens), an error message should be displayed.</li>
</ul>
""")
@pytest.mark.parametrize(("values", "expectation"), params_register_values_name_lastname)
def test_register_form_check_name_field(register, values, expectation):
    register.register_form_check_name_field(values, expectation)


@allure.id("RST-30")
@allure.feature("LastName Field")
@allure.suite("Register Form")
@allure.title("User Registration form LastName Field Validation")
@allure.description_html("""
Validate the 'Last Name' field in the User Registration form with various input substitutions. 
According to the documentation, the field should accept a range of 2 to 30 characters. 
The input field must contain at least 2 characters consisting of Cyrillic letters or a hyphen (-).
The system should verify the field and display an error if it does not meet the requirements.
<br><br><b>Expected result</b>:
<ul>
    <li>For valid Last names (2 to 30 characters consisting of Cyrillic letters or a hyphen), no error message should be displayed.</li>
    <li>For invalid Last names (less than 2 characters, more than 30 characters, or containing characters other than Cyrillic letters and hyphens), an error message should be displayed.</li>
</ul>
""")
@pytest.mark.parametrize(("values", "expectation"), params_register_values_name_lastname)
def test_register_form_check_lastname_field(register, values, expectation):
    register.register_form_check_lastname_field(values, expectation)


@allure.id("RST-31")
@allure.feature("Email Field")
@allure.suite("Register Form")
@allure.title("User Registration form Email Field Validation")
@allure.description_html("""
Validate the 'password' field in the User Registration form with various input substitutions.
<br><br><b>Expected result</b>:
<ul>
    <li>For valid email addresses, no error message should be displayed.</li>
    <li>For invalid email addresses (missing "@" symbol, incorrect format, etc.), an error message should be displayed.</li>
</ul>
""")
@pytest.mark.parametrize(("values", "expectation"), params_register_values_email)
def test_register_form_check_email_field(register, values, expectation):
    register.register_form_check_email_field(values, expectation)


@allure.id("RST-32")
@allure.feature("Phone Field")
@allure.suite("Register Form")
@allure.title("User Registration form Phone Field Validation")
@allure.description_html("""
Validate the 'Phone' field in the User Registration form with various input substitutions.
<br><br><b>Expected result</b>: The 'Phone' field in the User Registration form should be validated according to the following criteria:
<ul>
    <li>For valid phone numbers in the format "+[country code][phone number]", no error message should be displayed.</li>
    <li>For invalid phone numbers (incorrect format, missing country code, etc.), an error message should be displayed.</li>
</ul>
""")
@pytest.mark.parametrize(("values", "expectation"), params_register_values_phone)
def test_register_form_check_email_field(register, values, expectation):
    register.register_form_check_phone_field(values, expectation)


@allure.id("RST-33")
@allure.feature("Password Field")
@allure.suite("Register Form")
@allure.title("User Registration form password Field Validation")
@allure.description_html("""
This test case ensures that the system accurately evaluates user-entered passwords 
and displays appropriate error messages when the entered password does not meet the specified criteria:
    1) The system should display an error message for passwords with non-Latin characters.
    2) The system should display an error message for passwords without uppercase letters.
    3) The system should display an error message for passwords with less than 8 characters.
<br><br><b>Expected result</b>:
The password validation during user registration should follow these criteria:
<ol>
    <li>The system should display an error message for passwords with non-Latin characters.</li>
    <li>The system should display an error message for passwords without uppercase letters.</li>
    <li>The system should display an error message for passwords with less than 8 characters.</li>
</ol>                
""")
@pytest.mark.parametrize(("values", "expectation"), params_register_values_password)
def test_register_form_check_password_field(register, values, expectation):
    register.register_form_check_password_field(values, expectation)


@allure.id("RST-34")
@allure.feature("Confirm Password")
@allure.suite("Registration form")
@allure.title("User Registration Password Confirm Validation")
@allure.description_html("""
Validate the system's behavior when a user enters a confirmation password that does not match
the 'New Password' field. The test aims to ensure that the appropriate
error message 'Passwords do not match' is displayed below the 'Confirm Password' field
when such a mismatch occurs.
<br><br><b>Expected result</b>:
When a user enters a confirmation password that does not match the 'New Password' field:
The system should display the error message "Passwords do not match" below the 'Confirm Password' field.               
""")
@pytest.mark.parametrize(("value1", "value2", "expectation"), params_register_values_password_confirmed)
def test_register_form_check_confirm_password(register, value1, value2, expectation):
    register.register_form_check_confirm_password(value1, value2, expectation)


@allure.id("RST-35")
@allure.feature("Confirm form elements")
@allure.suite("Registration form")
@allure.title("Confirmation Email Form Element Presence Verification")
@allure.description_html("""
    Verify the presence of all necessary elements in the confirmation email form.
    This test ensures that after a user fills in valid values in all fields of the registration form
    and clicks the 'Register' button, all required elements are present and displayed correctly
    in the confirmation email form.
    <br><br><b>Expected result</b>:
    After a user fills in valid values in all fields of the registration form and clicks the 'Register' button:
    The confirmation email form should display all necessary elements correctly, including but not limited to:
    <li>Check code fields is displayed</li>
    <li>Check 'Change email' link</li>
    <li>Confirm code form</li>    
    """)
def test_register_form_confirm_check_code_elements(register):
    register.register_form_confirm_check_code_elements()


@allure.id("RST-36")
@allure.feature("Resend Code Button")
@allure.suite("Registration form")
@allure.title("Resend Code Button Availability")
@allure.description_html("""
Verify that the 'Resend Code' button appears in the confirmation email form after 120 seconds
when a user submits valid information in the registration form, clicks the 'Register' button,
and receives the initial verification code.
<br><br><b>Expected result</b>:
After a user submits valid information in the registration form, clicks the 'Register' button,
and receives the initial verification code:
<li>The 'Resend Code' button should become available and appear in the confirmation email form after 120 seconds.</li>
<li>This button allows the user to request a new verification code in case the initial code expires or is not received.</li>
""")
def test_register_form_confirm_check_repeat_btn(register):
    register.register_form_confirm_check_repeat_btn()


@allure.id("RST-37")
@allure.feature("Change Email button")
@allure.suite("Registration form")
@allure.title("Email Change Button Redirection")
@allure.description_html("""
Verify that clicking the 'Change Email' button in the email confirmation form redirects
the user to the registration form.
<br><br><b>Expected result</b>:
When a user clicks the 'Change Email' button in the email confirmation form:
The user should be redirected to the registration form, allowing them to modify their email address
and other registration details if needed.
""")
def test_register_form_confirm_change_email(register):
    register.register_form_confirm_change_email()


@allure.id("RST-38")
@allure.feature("incorrect verification code error")
@allure.suite("Registration form")
@allure.title("Error on Invalid Verification Code Submission")
@allure.description_html("""
Verify that an error message indicating the incorrect verification code appears when an
invalid code is entered in the verification code fields on the Email Confirmation form.
<br><br><b>Expected result</b>:
When an invalid verification code is entered in the verification code fields on the Email Confirmation form:
<li>The system should display an error message indicating that the entered verification code is incorrect.</li>
<li>This error message helps users understand that the provided code does not match the expected value.</li>
""")
def test_register_form_confirm_wrong_code_error(register):
    register.register_form_confirm_wrong_code_error()


@allure.id("RST-39")
@allure.feature("Email masked")
@allure.suite("Registration form")
@allure.title("Masked Email Display on Email Confirmation Form")
@allure.description_html("""
Verify that the entered email address is displayed in a masked format on the
Email Confirmation form after it has been provided during the registration process.
<br><br><b>Expected result</b>:
After the email address has been provided during the registration process and is displayed on the Email Confirmation form: 
The entered email address should be displayed in a masked format (e.g., "user***@example.com") on the Email Confirmation form.         
""")
@allure.issue("https://github.com/eeefimov/RostelecomTesting/issues/8#issue-1848585288, GitHub: Email does not Masked "
              "on Email Confirmation Form")
def test_register_form_confirm_mail_masked(register):
    register.register_form_confirm_mail_masked()