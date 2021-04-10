from pages.category_page_iphone import CategoryPage
from pages.category_page_watch import CategoryPageWatch


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.category_page_iphone = CategoryPage(self.driver)
        self.category_page_watch = CategoryPageWatch(self.driver)
