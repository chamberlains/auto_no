import unittest

from selenium import webdriver

from config.driver_config import DriverConfig


class BaseTest(unittest.TestCase):
    def __init__(self, driver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = driver


class UsualTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.driver = cls.open_driver()
        cls.driver_config = DriverConfig()
        cls.open_home_page(cls)

    def open_home_page(self):
        self.driver.get(self.driver_config.origin_url)
        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*self.driver_config.toast_locators))
        if 'sso' in self.driver.current_url:
            self.driver.add_cookie(self.driver_config.iuc_cookie)
            self.driver.refresh()
        self.driver.get(self.driver_config.url)
        self.driver.add_cookie(self.driver_config.cookie)
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @staticmethod
    def open_driver():
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_driver = webdriver.Chrome(options=options)
        return chrome_driver
