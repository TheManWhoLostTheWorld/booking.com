from base.base_test import BaseTest
import time

class TestStays(BaseTest):

    def test_open_stays_page(self):
        self.stays_page.open()
        self.stays_page.click_stays()

    def test_search_only_city(self):
        self.stays_page.open()
        self.stays_page.cancel_registration_window()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination("Hamburg")
        self.stays_page.click_search()
        self.stays_page.cancel_registration_window()
        self.stays_page.proof_location("Hamburg")

    def test_dropdown_click(self):
        self.stays_page.open()
        self.stays_page.cancel_registration_window()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination_by_dropdown("Bei")
        self.stays_page.dropdown_destination_click("Beirut")
        self.stays_page.click_search()
        self.stays_page.cancel_registration_window()
        self.stays_page.proof_location("Beirut")

    def test_search_specific_hotel(self):
        self.stays_page.open()
        self.stays_page.cancel_registration_window()
        self.stays_page.accept_cookies()
        self.stays_page.add_hotel("Radisson Blu")
        self.stays_page.click_search()
        self.stays_page.cancel_registration_window()
        self.stays_page.proof_hotel("Radisson Blu")

    def test_search_country_with_dates(self):
        self.stays_page.open()
        self.stays_page.cancel_registration_window()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination("Germany")
        self.stays_page.accept_cookies()
        self.calendar.open()
        self.calendar.set_date(25, 9, 2025)
        self.calendar.set_date(5, 10, 2025)
        self.people.set_people(2, 2)
        self.people.ages(5, 12)
        self.stays_page.click_search()
        self.stays_page.cancel_registration_window()
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


