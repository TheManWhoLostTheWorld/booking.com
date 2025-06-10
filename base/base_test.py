from pages.stays_page import StaysPage
from pages.car_rental_page import CarRentalsPage
from helpers.calendar_helper import CalendarHelper
from helpers.people_helper import PeopleHelper
from helpers.ui_helper import UiHelper
from helpers.filter_helper import CheckBoxHelper

class BaseTest:

    def setup_method(self):
       self.stays_page = StaysPage(self.driver)
       self.car_rental_page = CarRentalsPage(self.driver)
       self.calendar = CalendarHelper(self.driver)
       self.people = PeopleHelper(self.driver)
       self.ui = UiHelper(self.driver)
       self.checkbox = CheckBoxHelper(self.driver)