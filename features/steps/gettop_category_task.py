from behave import given, when, then


@given('Open GetTop Page')
def open_gettop(context):
    context.app.category_page_iphone.open_gettop()


@when('Navigate to iPhone Category')
def iphone_page(context):
    context.app.category_page_iphone.iphone_page()


@then('Verify all Items Category')
def verify_items_category(context):
    context.app.category_page_iphone.verify_items_category()


@then('Verify number of Items')
def verify_number_items(context):
    context.app.category_page_iphone.verify_number_items()


@then('Verify every Item Category, Name and Price')
def verify_category_name_price(context):
    context.app.category_page_iphone.verify_category_name_price()


@then('Hover on Item Picture')
def hover_item_picture(context):
    context.app.category_page_iphone.hover_item_picture()


@then('Click on Quick View Button')
def quick_view(context):
    context.app.category_page_iphone.quick_view()


@then('Close the Quick View')
def close_quick_view(context):
    context.app.category_page_iphone.close_quick_view()


@then('Add Item to Cart')
def add_item_to_cart(context):
    context.app.category_page_iphone.add_item_to_cart()