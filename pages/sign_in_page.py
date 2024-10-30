from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):

    SIGN_IN_HEADER = (By.CSS_SELECTOR, 'h1 span')
    #TC_LINK = (By.XPATH, "//a[text()='Terms conditions']")
    TC_LINK = (By.CSS_SELECTOR, 'a[href*="/c/terms-conditions"]')

    def click_tc_link(self):
        self.click(*self.TC_LINK)

    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions/' )

    def verify_signin_opened(self):
        expected_text = 'Sign into your Target account'
        self.verify_text(expected_text, *self.SIGN_IN_HEADER)

