from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In form opened')
def verify_signin_opened(context):
    context.app.sign_in_page.verify_signin_opened()