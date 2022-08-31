from locators.portal import PortalLocators
from pages.BasePage import BasePage


class PortalPage(BasePage):
    def __init__(self, driver, *args, **kwargs):
        super().__init__(driver, *args, **kwargs)
        self.portal_locators = PortalLocators()

    def get_navigate_title(self):
        elems = self.get_elements(self.portal_locators.NAVIGATE_BAR)
        return self.get_element_text(elems)

    def click_search_bar(self):
        self.click(self.portal_locators.TOP_SEARCH_INPUT)

    def input_search_word(self, text):
        self.update_text(self.portal_locators.TOP_SEARCH_INPUT, text)
