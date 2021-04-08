from pages.category_page_iphone import CategoryPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.category_page_iphone = CategoryPage(self.driver)
