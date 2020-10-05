from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")

    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR,  "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div > h1")
    ORDERED_PRODUCT_NAME = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong")

