from tests.attendance.vacation import VacationTest
from tests.base_test import UsualTest


class TestAttendance(UsualTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.vacation_test = VacationTest(cls.driver)

    def test_01_demo(self):
        self.vacation_test.into_apply_page()
