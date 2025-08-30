from base.base_test import BaseTest
import time

class TestStays(BaseTest):

    def test_open_stays_page(self):
        self.stays_page.open()
        self.stays_page.click_stays()

    def test_search_only_city(self):
        self.stays_page.open()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination("Istanbul")
        self.stays_page.click_search()
        self.stays_page.proof_location("Istanbul")

    def test_dropdown_click(self):
        self.stays_page.open()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination("Bel")
        self.stays_page.dropdown_destination_click("Belgrade")
        self.stays_page.click_search()
        self.stays_page.proof_location("Belgrade")

    def test_search_vacation_country(self):
        self.stays_page.open()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination("Germany")
        self.calendar.open()
        self.calendar.set_date(1, 6, 2025)
        self.calendar.set_date(12, 6, 2025)
        self.people.set_people(2, 2)
        self.people.ages(5, 12)
        self.stays_page.click_search()
        self.stays_page.proof_location("Germany")

    def test_search_vacation_city(self):
        self.stays_page.open()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination("Paris")
        self.calendar.open()
        self.calendar.set_date(8, 6, 2025)
        self.calendar.set_date(15, 6, 2025)
        self.people.set_people(2, 3)
        self.people.ages(0, 8, 17)
        self.stays_page.click_search()
        self.stays_page.proof_location("Paris")

    def test_scroll_to_element(self):
        self.stays_page.open()
        self.ui.scroll_to(("xpath", "//button[@id='CITY-tab-trigger']"))
        time.sleep(3)


