from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):

    SIGN_IN_HEADER = (By.CSS_SELECTOR, 'h1 span')
    #TC_LINK = (By.XPATH, "//a[text()='Terms conditions']")
    TC_LINK = (By.CSS_SELECTOR, 'a[href*="/c/terms-conditions"]')
    EMAIL_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    SIGN_IN_BUTTON = (By.ID, 'login')
    SORRY_PAGE = (By.XPATH , "//div[text()='Sorry, something went wrong. Please try again']")

    def click_tc_link(self):
        self.click(*self.TC_LINK)

    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions/' )

    def verify_signin_opened(self):
        expected_text = 'Sign into your Target account'
        self.verify_text(expected_text, *self.SIGN_IN_HEADER)

    def input_incorrect_password_and_email(self):
        self.input_text('example@gmail.com', *self.EMAIL_FIELD)
        self.input_text('careerist', *self.PASSWORD_FIELD)

    def click_sign_in_button(self):
        self.wait_to_be_clickable_click(*self.SIGN_IN_BUTTON )

    def verify_sorry_page(self):
        expected_text = 'Sorry, something went wrong. Please try again'
        self.verify_text(expected_text, *self.SORRY_PAGE)

