from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
VIEW_CART_AND_CHECKOUT_BTN = (By.CSS_SELECTOR, '[href="/cart"]')
ITEM_TEXT = (By.CSS_SELECTOR, 'div[class*="h-text-grayDark"] span')
ACTUAL_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')

@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*VIEW_CART_AND_CHECKOUT_BTN).click()


@then('Verify cart has 1 item(s)')
def verify_one_item_added(context):
    actual_result = context.driver.find_element(*ITEM_TEXT).text
    assert '1 item' in actual_result, f'Expected 1 item but got {actual_result}'

@then('Verify cart has correct product')
def verify_cart_product(context):
    actual_product_name = context.driver.find_element(*ACTUAL_PRODUCT_NAME).text
    assert actual_product_name in context.product_name, f'Expected {context.product_name} but got {actual_product_name}'

@then ('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Side navigation product name not visible'
    )

#
# @then('Verify that correct search results shown for {product}')
# def verify_results(context, product):
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text