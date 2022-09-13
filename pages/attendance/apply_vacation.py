from locators.attendance.vacation import VacationLocators
from pages.attendance import AttendancePage


class VacationPage(AttendancePage):
    def into_apple_page(self):
        elems = self.find_elements_by_text(VacationLocators.APPLE_VACATION_BUTTON, "新增休假")
        self.click(elems)
