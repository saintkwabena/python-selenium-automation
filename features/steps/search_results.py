from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    sleep(5)
    context.driver.execute_script("window.scroll(0, 500);") # Scroll down to 500px
    #context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()


@when('Store product name')
def store_product_name(context):
    sleep(5)
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
    sleep(3)

@then('Verify that correct search results shown for {product}')
def verify_results(context, product):
    context.app.search_results_page.verify_results(product)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)