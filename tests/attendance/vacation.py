from pages.attendance.apply_vacation import VacationPage
from tests.base_test import BaseTest


class VacationTest(BaseTest):
    def __init__(self, driver, *args, **kwargs):
        super().__init__(driver, *args, **kwargs)
        self.vacation_page = VacationPage(driver)

    def into_apply_page(self):
        self.dashboard_page.into_attendance_page()
        self.vacation_page.into_vacation_page()
        self.vacation_page.into_apple_page()
