from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def check_that_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button not displayed"

    def compare_price_in_basket_and_product_price(self):
        product_price = self.is_element_present(*ProductPageLocators.PRODUCT_PRICE)
        price_in_basket = self.is_element_present(*ProductPageLocators.PRICE_IN_BASKET)
        assert product_price == price_in_basket, "Product price and price in basket are different"
