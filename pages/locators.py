from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")

    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR,"#id_login-password")
