from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Invalid URL(""login"" not in URL)"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELD), \
            "E-mail field for Login is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), \
            "Password field for Login is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REG_EMAIL_FIELD), "E-mail field for registration is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REG_PASSWORD_FIELD), "Password field for Registration is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REG_CONFIRM_PASSWORD_FIELD), "Confirm Password field for Registration is not presented"
