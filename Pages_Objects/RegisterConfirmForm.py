from selenium.webdriver.common.by import By


class RConfirmForm:
    r_confirm_form = (By.CLASS_NAME, "card-container__wrapper")
    r_confirm_codemail_change_mail_link = (By.CLASS_NAME, "register-confirm-form__back-btn")
    r_confirm_codemail_code_field = (By.CSS_SELECTOR, "#rt-code-0")
    r_confirm_codemail_repeat_code_btn = (By.CLASS_NAME, "code-input-container__resend")
    r_confirm_codemail_error_wrong_code = (By.CSS_SELECTOR, "#form-error-message")
    r_confirm_codemail_hide_mail = (By.CLASS_NAME, "register-confirm-form-container__desc")


