from data.portal import search_data
from tests.base_test import UsualTest
from tests.portal.portal_test import PortalTest


class portal_test(UsualTest):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.portal_test = PortalTest(cls.driver)

    def test_01_demo(self):
        for key, value in search_data().items():
            self.portal_test.input_search(value.search_text)
