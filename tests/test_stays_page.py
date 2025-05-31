from base.base_test import BaseTest
import time

class TestStays(BaseTest):

    def test_open_stays_page(self):
        self.stays_page.open()
        self.stays_page.click_stays()

    def test_open_calendar(self):
        self.stays_page.open()
        self.stays_page.accept_cookies()
        self.calendar.open()
        self.calendar.set_date(19, 5, 2025)

    def test_select_people(self):
        self.stays_page.open()
        self.stays_page.accept_cookies()
        self.stays_page.open_select_people_popup()
        self.people.set_people(4, 2)
        self.people.ages(4, 3)

    def test_search_vacation(self):
        self.stays_page.open()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination("Germany")
        self.calendar.open()
        self.calendar.set_date(1, 6, 2025)
        time.sleep(3)
        self.calendar.set_date(12, 6, 2025)
        time.sleep(3)

        self.people.set_people(2, 2)
        self.people.ages(5, 12)
        self.stays_page.click_search()
        self.stays_page.prof_location("Germany")

