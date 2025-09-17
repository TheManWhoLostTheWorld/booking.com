from base.base_test import BaseTest
import pytest
import time

class TestStays(BaseTest):

    @pytest.mark.flaky(reruns=2, reruns_delay=2, max_reruns=3)
    @pytest.mark.regression
    def test_open_stays_page(self):
        self.stays_page.open()
        self.stays_page.click_stays()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_search_city(self):
        self.stays_page.open()
        self.stays_page.cancel_registration_window()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination("Hamburg")
        self.stays_page.accept_cookies()
        self.calendar.open()
        self.calendar.set_date(25, 10, 2025)
        self.calendar.set_date(5, 11, 2025)
        self.people.set_people(2, 0)
        self.stays_page.click_search()
        self.stays_page.cancel_registration_window()
        self.stays_page.proof_location("Hamburg")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_dropdown_click(self):
        self.stays_page.open()
        self.stays_page.cancel_registration_window()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination_by_dropdown("Bei")
        self.stays_page.dropdown_destination_click("Beirut")
        self.stays_page.accept_cookies()
        self.calendar.open()
        self.calendar.set_date(10, 1, 2026)
        self.calendar.set_date(5, 2, 2026)
        self.people.set_people(3, 3)
        self.people.ages(5, 12, 17)
        self.stays_page.click_search()
        self.stays_page.cancel_registration_window()
        self.stays_page.proof_location("Beirut")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_search_specific_hotel(self):
        self.stays_page.open()
        self.stays_page.cancel_registration_window()
        self.stays_page.accept_cookies()
        self.stays_page.add_hotel("Radisson Blu")
        self.stays_page.accept_cookies()
        self.calendar.open()
        self.calendar.set_date(7, 3, 2026)
        self.calendar.set_date(15, 3, 2026)
        self.people.set_people(2, 1)
        self.people.ages(2)
        self.stays_page.click_search()
        self.stays_page.cancel_registration_window()
        self.stays_page.proof_hotel("Radisson Blu")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_search_country(self):
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

    @pytest.mark.negative
    @pytest.mark.regression
    def test_search_date_in_the_past(self):
        self.stays_page.open()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination("Paris")
        self.stays_page.accept_cookies()
        self.calendar.open()
        self.calendar.set_date(8, 6, 2025)
        self.calendar.set_date(15, 6, 2025)
        self.people.set_people(2, 3)
        self.people.ages(0, 8, 17)
        self.stays_page.click_search()
        self.stays_page.proof_location("Paris")

    # def test_scroll_to_element(self):
    #     self.stays_page.open()
    #     self.ui.scroll_to(("xpath", "//button[@id='CITY-tab-trigger']"))
    #     time.sleep(3)


