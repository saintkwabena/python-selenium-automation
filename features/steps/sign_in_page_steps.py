from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#
# @given('Open sign in page')
# def open_sign_in_page(context):
#     context.app.main_page.open_main()
#     context.app.header.click_signin_btn()
#     context.app.header.click_side_nav_btn()
#     sleep(5)

@then('Verify Sign In form opened')
def verify_signin_opened(context):
    context.app.sign_in_page.verify_signin_opened()

