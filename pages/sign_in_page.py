from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):

    SIGN_IN_HEADER = (By.CSS_SELECTOR, 'h1 span')

    def verify_signin_opened(self):
        expected_text = 'Sign into your Target account'
        self.verify_text(expected_text, *self.SIGN_IN_HEADER)

