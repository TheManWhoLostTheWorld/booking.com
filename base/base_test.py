from pages.stays_page import StaysPage
from pages.car_rental_page import CarRentalsPage
from helpers.calendar_helper import CalendarHelper

class BaseTest:

    def setup_method(self):
       self.stays_page = StaysPage(self.driver)
       self.car_rental_page = CarRentalsPage(self.driver)
       self.calendar = CalendarHelper(self.driver)