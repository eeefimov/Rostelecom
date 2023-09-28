import pytest
import random
import string


def randomize_phone():
    random_code = ''.join(random.choice('0123456789') for _ in range(2))
    random_digits = ''.join(random.choice('0123456789') for _ in range(8))
    phone_number = f"8{random_code}{random_digits}"
    return phone_number


def randomize_string(str_type, number: int):
    """Generate a random string of the specified type and length."""
    symbols = str_type
    random_string = "".join(random.choice(symbols) for _ in range(number))
    return random_string


def randomize_cyrillic_string(number: int):
    """Generate a random Cyrillic string of the specified length."""
    cyrillic_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    random_string = "".join(random.choice(cyrillic_chars) for _ in range(number))
    return random_string


def randomize_chinese_string(number: int):
    """Generate a random Chinese string of the specified length."""
    chinese_chars = '的一是不了人我在有他这为之大来以个中上们'
    random_string = "".join(random.choice(chinese_chars) for _ in range(number))
    return random_string


def randomize_special_string(number: int):
    special_chars = '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'
    random_string = "".join(random.choice(special_chars) for _ in range(number))
    return random_string


# Test parameters for checking the correctness of the tab names on the authorization form.
params_auth_form_tabs_name_requirement = [
    pytest.param("t-btn-tab-phone", "Номер", id="Phone"),
    pytest.param("t-btn-tab-mail", "Почта", id="Email"),
    pytest.param("t-btn-tab-login", "Логин", id="Login"),
    pytest.param("t-btn-tab-ls", "Лицевой счёт", id="Personal Account")
]

# Test parameters for checking the values and labels of the authorization form when selecting different tabs.
params_auth_form_value_auto_tab = [
    pytest.param([randomize_phone(), "Телефон", "t-btn-tab-phone"], id="Phone"),
    pytest.param(["mail@mail.com", "Почта", "t-btn-tab-mail"], id="Email"),
    pytest.param([randomize_string(string.ascii_letters, 10), "Логин", "t-btn-tab-login"], id="Login"),
    pytest.param([randomize_string(string.digits, 12), "Лицевой счёт", "t-btn-tab-ls"], id="Personal account")
]

# Test parameters for checking the labels of tabs.
params_label_tabs = [
    pytest.param("Мобильный телефон", "Телефон", id="Mobile Label"),
    pytest.param("Электронная почта", "Почта", id="Email Label"),
    pytest.param("Логин", "Логин", id="PersonalCabinet Label"),
    pytest.param("Лицевой счёт", "Лицевой счёт", id="LC Label")
]

# Test parameters for setting window size and check left side block is displayed
params_window_size = [
    pytest.param(1920, 1080, id="HDTV"),
    pytest.param(1024, 768, id="Desktop"),
    pytest.param(1023, 768, id="Desktop -1")
]

# Test parameters for checking invalid phone number and password combinations.
params_wrong_phone_number_pass = [
    pytest.param(randomize_phone(), "123!@#QWERTYasdfg", False, id="Invalid Phone valid Pass"),
    pytest.param(79217472514, "@#QWERTYasdfg", False, id="Valid Phone invalid Pass"),
    pytest.param(79217472514, "", False, id="Valid Phone Empty Pass"),
    pytest.param(randomize_phone(), "@#QWERTYasdfg", False, id="Invalid Phone invalid Pass"),
    pytest.param("", "@#QWERTYasdfg", False, id="Empty Phone valid Pass")
]

# Test parameters for checking invalid email and password combinations.
params_wrong_email_pass = [
    pytest.param("dobr@mail.ru", "123!@#QWERTYasdfg", False, id="Invalid Email valid Pass"),
    pytest.param("moybobrdobr@mail.ru", "@#QWERTYasdfg", False, id="Valid Email invalid Pass"),
    pytest.param("moybobrdobr@mail.ru", "", False, id="Valid Email Empty Pass"),
    pytest.param("", "123!@#QWERTYasdfg", False, id="Empty Email valid Pass")
]

# Test parameters for checking invalid personal account (LS) and password combinations.
params_wrong_ls_pass = [
    pytest.param(278015603030, "123!@#QWERTYasdfg", False, id="Invalid LS valid Pass"),
    pytest.param(278015603034, "@#QWERTYasdfg", False, id="Valid LS invalid Pass"),
    pytest.param(278015603034, "", False, id="Valid LS Empty Pass"),
    pytest.param("", "123!@#QWERTYasdfg", False, id="Empty LS valid Pass")
]

# Test parameters for checking various name and last name inputs for registration.
params_register_values_name_lastname = [
    pytest.param(randomize_cyrillic_string(1), False, id="One char cyrillic"),
    pytest.param(randomize_cyrillic_string(2), True, id="Two chars cyrillic"),
    pytest.param(randomize_cyrillic_string(30), True, id="30 chars cyrillic"),
    pytest.param(randomize_cyrillic_string(31), False, id="31 chars cyrillic"),
    pytest.param("", False, id="Empty")
]

# Test parameters for checking various email inputs for registration.
params_register_values_email = [
    pytest.param("mail@mail.com", True, id="mail@mail.com"),
    pytest.param("m@mail.com", True, id="m@mail.com"),
    pytest.param("mail@m.com", True, id="mail@m.com"),
    pytest.param("mail@ma.com", True, id="mail@ma.com"),
    pytest.param("", False, id="Empty email")
]

# Test parameters for checking various phone inputs for registration.
params_register_values_phone = [
    pytest.param("+79991234567", True, id="Valid phone number: +79991234567"),
    pytest.param("", False, id="Empty number"),
    pytest.param("+375291234567", True, id="Valid phone number: +375291234567"),
    pytest.param(79991234567, True, id="Valid phone number int: 79991234567"),
    pytest.param("89991234567", True, id="Valid phone number: 89991234567"),
    pytest.param("9991234567", True, id="Valid phone number: 9991234567"),
    pytest.param("+7999123456", False, id="INValid phone number: +7999123456"),
    pytest.param("+7(999)1234567", True, id="Valid phone number: +7(999)1234567"),
    pytest.param("+7(999)123-45-67", True, id="Valid phone number: +7(999)123-45-67")
]

# Test parameters for checking various password inputs for registration.
params_register_values_password = [
    pytest.param("Abcdefgh", False, id="Password without numbers"),
    pytest.param("Abcd1234", True, id="Valid password with numbers"),
    pytest.param("abcdefgh", False, id="Password without uppercase letter"),
    pytest.param("ABCDEFGH", False, id="Password without lowercase letter"),
    pytest.param("Abcd", False, id="Password less than 8 characters"),
    pytest.param("12345678", False, id="Password without letters"),
    pytest.param("абвгдеёж", False, id="Password with non-Latin characters"),
    pytest.param("Abcd!@#$", True, id="Password with special characters"),
    pytest.param("Abcd1234Abcd12341234", True, id="20 Valid password with numbers"),
    pytest.param("Abcd1234Abcd123412341", False, id="21 Valid password with numbers"),
    pytest.param("", False, id="Empty password")
]

# Test parameters for checking password confirmation during registration.
params_register_values_password_confirmed = [
    pytest.param("Abcd1234", "Abcd1234", True, id="Valid password"),
    pytest.param("Abcd1234", "", False, id="Valid password and empty"),
    pytest.param("Abcd1234", "1234Abcd", False, id="Valid password and wrong")
]
