import time

from utils import condition_wait

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver, *args, **kwargs):
        self.driver = driver

    def get_elements(self, locators, index=0, timeout=10):
        return WebDriverWait(self, timeout, ignored_exceptions=(TimeoutException,)).until(
            lambda x: x.get_elems(locators, index))

    def get_elems(self, locators, index):
        elems = self.driver.find_elements(*locators)
        if index is not None and elems:
            return elems[index]
        if index is None:
            return elems

    def update_text(self, locators, text, index=0):
        if isinstance(locators, tuple):
            locators = self.get_elements(locators, index)
        try:
            locators.clear()
            locators.send_keys(Keys.BACK_SPACE * 2 * (len(locators.get_attribute("value")) + 3))
        except StaleElementReferenceException:
            time.sleep(0.5)
            locators.clear()
            locators.send_keys(Keys.BACK_SPACE * 2 * (len(locators.get_attribute("value")) + 3))
        locators.send_keys(text + Keys.ENTER)

    def click(self, locators, index=0):
        if isinstance(locators, tuple):
            locators = self.get_elements(locators, index)
        self.scroll_to_element(locators)
        ActionChains(self.driver).click(locators).perform()

    def get_element_text(self, locators, index=0):
        if isinstance(locators, tuple):
            locators = self.get_elements(locators, index)

        return locators.get_attribute("innerText")

    def scroll_to_element(self, element):
        try:
            element_location_y = element.location["y"]
        except Exception:
            return False

        element_location_y = element_location_y - 130
        if element_location_y < 0:
            element_location_y = 0
        scroll_script = "window.scrollTo(%s, %s);" % (
            element.location["x"], element_location_y
        )
        try:
            self.driver.execute_script(scroll_script)
            return True
        except Exception:
            return False

    def find_elements_by_text(self, locators, text, root, timeout=10):
        root = root or self.driver
        return WebDriverWait(root, timeout).until(condition_wait.element_with_text(locators, text))

    def reveal(self):
        pass
