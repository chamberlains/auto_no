from pages.portal_page import PortalPage
from tests.base_test import BaseTest, UsualTest


class PortalTest(BaseTest):
    def __init__(self, driver, *args, **kwargs):
        super().__init__(driver, *args, **kwargs)
        self.portal_page = PortalPage(driver)

    def input_search(self, text):   #
        self.portal_page.click_search_bar()
        self.portal_page.input_search_word(text)
