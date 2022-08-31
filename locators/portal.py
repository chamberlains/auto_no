from selenium.webdriver.common.by import By


class PortalLocators:
    NAVIGATE_BAR = (By.CSS_SELECTOR, "ul.nav-list li.nav-item")
    TOP_SEARCH_INPUT = (By.CSS_SELECTOR, "div.search-input-wrapper input")
