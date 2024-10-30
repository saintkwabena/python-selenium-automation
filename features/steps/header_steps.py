from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#
# @when('Click sign In')
# def click_sign_in(context):
#     context.app.header.click_signin_btn()
#     sleep(3)

@when('Click Sign In from right navigation')
def click_sign_in_nav(context):
    context.app.header.click_side_nav_btn()

