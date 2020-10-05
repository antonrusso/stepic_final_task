from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def check_that_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button not displayed"

    def compare_price_in_basket_and_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)

        assert product_price.text == price_in_basket.text, \
            f"Product price {product_price.text} and price in basket{price_in_basket.text} are different"


