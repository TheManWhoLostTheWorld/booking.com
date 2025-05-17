from base.base_test import BaseTest
import time

class TestStays(BaseTest):

    def test_open_stays_page(self):
        self.stays_page.open()
        self.stays_page.click_stays()