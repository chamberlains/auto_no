from locators.dashboard import DashboardLocators
from pages.BasePage import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver, *args, **kwargs):
        super().__init__(driver, *args, **kwargs)

    def into_attendance_page(self):
        elem = self.find_elements_by_text(DashboardLocators.NAVIGATE_BAR, "考勤")
        self.click(elem)
