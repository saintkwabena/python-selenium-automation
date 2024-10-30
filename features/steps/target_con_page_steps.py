from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.main_page.open_main()
    context.app.header.click_signin_btn()
    context.app.header.click_side_nav_btn()
    sleep(5)


@given('Store original window')
def store_window(context):
    context.original_window = context.app.target_app_page.get_current_window()
    print('Original window: ', context.original_window)

@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.sign_in_page.click_tc_link()

@when('Switch to the newly opened window')
def switch_to_window(context):
    context.app.sign_in_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.sign_in_page.verify_tc_opened()

@then('Close new window')
def close_new_window(context):
    context.app.target_app_page.close()
    sleep(5)

@then ('Switch back to original')
def switch_to_original(context):
    context.driver.switch_to.window(context.original_window)
    sleep(5)


