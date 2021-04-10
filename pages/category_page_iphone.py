from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class CategoryPage(Page):
    IPHONE_CATEGORY = (By.CSS_SELECTOR, '#menu-item-469')
    NUMBER_RESULTS = (By.CSS_SELECTOR, 'p.woocommerce-result-count')
    ITEM = (By.CSS_SELECTOR, 'div.product-small .col-inner')
    ITEM_NAME = (By.CSS_SELECTOR, 'div.shop-container .name')
    ITEM_CATEGORY = (By.CSS_SELECTOR, 'div.shop-container .category')
    ITEM_PRICE = (By.CSS_SELECTOR, 'div.shop-container .amount')
    ITEM_IMAGE = (By.CSS_SELECTOR, 'div.box-image')
    QUICK_VIEW_BUTTON = (By.CSS_SELECTOR, 'a.quick-view')
    QUICK_VIEW_CLOSE = (By.CSS_SELECTOR, 'div.mfp-wrap .mfp-close')
    ADD_TO_CART_QUICK_VIEW = (By.CSS_SELECTOR, 'form.cart .single_add_to_cart_button')

    def open_gettop(self):
        self.open_url('https://gettop.us/')

    def iphone_page(self):
        self.click(*self.IPHONE_CATEGORY)

    def verify_items_category(self):
        expected_name = 'iPhone'
        all_items_name = self.driver.find_elements(*self.ITEM_NAME)
        for i in all_items_name:
            assert expected_name in i.text, f'Expected{expected_name}, but got {i}'
            print(i.text)  # for demo purposes

    def verify_number_items(self):
        number_results = self.driver.find_element(*self.NUMBER_RESULTS).text
        count_items = len(self.driver.find_elements(*self.ITEM))
        assert str(count_items) in number_results, f'Expected {number_results}, but got {count_items}'

    def verify_category_name_price(self):
        all_items = self.driver.find_elements(*self.ITEM)

        for i in range(len(all_items)):
            print('==============')  # for demo purposes

            single_item_category = self.driver.find_elements(*self.ITEM_CATEGORY)[i].text
            print(single_item_category) # for demo purposes
            assert 'IPHONE' in single_item_category, f'Expected "IPHONE", but got {single_item_category}'

            single_item_name = self.driver.find_elements(*self.ITEM_NAME)[i].text
            print(single_item_name)  # for demo purposes
            assert 'iPhone' in single_item_name, f'Expected "iPhone", but got {single_item_name}'

            single_item_price = self.driver.find_elements(*self.ITEM_PRICE)[i].text
            print(single_item_price)  # for demo purposes
            assert '$' in single_item_price, f'Expected a price, but got {single_item_price}'
        print('==============')  # for demo purposes

    def hover_item_picture(self):
        self.hover_object(*self.ITEM_IMAGE)

    def quick_view(self):
        self.wait_for_element_click(*self.QUICK_VIEW_BUTTON)
        sleep(3)    # for demo purposes

    def close_quick_view(self):
        self.click(*self.QUICK_VIEW_CLOSE)

    def add_item_to_cart(self):
        self.click(*self.ADD_TO_CART_QUICK_VIEW)
        sleep(3)  # for demo purposes