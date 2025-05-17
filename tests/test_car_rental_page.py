from base.base_test import BaseTest
import time


class TestCarRentalPage(BaseTest):


    def test_open_car_rental_page(self):
        self.car_rental_page.open()
        self.car_rental_page.open_car_rental_page()
