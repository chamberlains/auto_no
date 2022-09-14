from locators.attendance import AttendanceLocators
from pages.BasePage import BasePage


class AttendancePage(BasePage):
    def __init__(self, driver, *args, **kwargs):
        super().__init__(driver, *args, **kwargs)

    def into_vacation_page(self):
        elem = self.find_elements_by_text(AttendanceLocators.MENU_ITEMS, "休假公出")
        self.click(elem)
