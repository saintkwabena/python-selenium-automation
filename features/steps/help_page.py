from behave import given, when, then


@given('Open Help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()

@when('Select Help topic {option}')
def select_topic(context, option):
    context.app.help_page.select_topic(option)


@then('Verify help {expected_header_text} page opened')
def verify_returns_opened(context, expected_header_text):
    context.app.help_page.verify_header(expected_header_text)