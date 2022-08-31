from selenium.webdriver.support import expected_conditions


class element_with_text:
    def __init__(self, locators, text):
        self.locators = locators
        self.text = text

    def __call__(self, driver):
        elems = driver.find_elements(*self.locators)
        for elem in elems:
            if self.text in elem.text:
                return elem
        return False
