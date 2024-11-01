from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.main_page.open_main()
    context.app.header.click_signin_btn()
    context.app.header.click_side_nav_btn()
    sleep(5)

@given('incorrect email and password combination')
def incorrect_email_and_password(context):
    context.app.sign_in_page.input_incorrect_password_and_email()

@then ('Clicks signin with password button')
def click_sign_in_btn(context):
    context.app.sign_in_page.click_sign_in_button()

@then('Verify that “Sorry, something went wrong. Please try again” message is shown')
def verify_sorry_page(context):
    context.app.sign_in_page.verify_sorry_page()

@then('Verify Sign In form opened')
def verify_signin_opened(context):
    context.app.sign_in_page.verify_signin_opened()
    sleep(2)
