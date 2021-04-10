from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class CategoryPageWatch(Page):
    WATCH_CATEGORY = (By.CSS_SELECTOR, '#menu-item-471')
    WATCH_MENU_ITEMS = (By.CSS_SELECTOR, '#menu-item-471 .sub-menu .menu-item')
    ITEM_TITLE_IN_PAGE = (By.CSS_SELECTOR, 'h1.product-title')

    def hover_watch_menu(self):
        self.hover_object(*self.WATCH_CATEGORY)
        sleep(1)

    def verify_items_watch_dropdown(self):
        assert self.driver.find_elements(*self.WATCH_MENU_ITEMS), f'There are no items in the WATCH dropdown menu'

        # or another approach, where we can check if there are items with the name "Watch Series"
        all_items = self.driver.find_elements(*self.WATCH_MENU_ITEMS)

        for i in range(len(all_items)):
            single_item = all_items[i].text
            print(single_item)  # for demo purposes
            assert 'Watch Series' in single_item, f'Expected "Watch Series" items, but got {single_item}'

    def open_items_and_verify(self):
        all_items = self.driver.find_elements(*self.WATCH_MENU_ITEMS)

        for i in range(len(all_items)):
            current_item = self.driver.find_elements(*self.WATCH_MENU_ITEMS)[i]
            item_name = current_item.text
            print(item_name)  # for demo purposes
            print("--------------")  # for demo purposes
            current_item.click()
            title_text = self.driver.find_element(*self.ITEM_TITLE_IN_PAGE).text
            print(title_text)  # for demo purposes
            sleep(1)
            print('==============')  # for demo purposes
            self.verify_text(item_name, *self.ITEM_TITLE_IN_PAGE)
            self.hover_object(*self.WATCH_CATEGORY)
            sleep(1)

