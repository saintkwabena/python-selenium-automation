from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGNIN_BTN = (By.CSS_SELECTOR, 'a[data-test="@web/AccountLink"]')
    SIGNIN_BTN_SIDE_NAV = (By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]')

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6) # wait for search results page to load

    def click_cart(self):
        self.wait_to_be_clickable_click(*self.CART_BTN)

    def click_signin_btn(self):
        self.wait_to_be_clickable_click(*self.SIGNIN_BTN)

    def click_side_nav_btn(self):
        self.wait_to_be_clickable_click(*self.SIGNIN_BTN_SIDE_NAV)
