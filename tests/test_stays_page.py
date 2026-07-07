from base.base_test import BaseTest
import pytest
import time

class TestStays(BaseTest):

    @pytest.mark.flaky(reruns=2, reruns_delay=2, max_reruns=3)
    @pytest.mark.regression
    def test_open_stays_page(self): # this test shows how to deal with flaky tests. In this configuration it will never pass
        self.stays_page.open()
        self.stays_page.click_stays()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_search_city(self):
        self.stays_page.open()
        self.stays_page.cancel_registration_window()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination("Hamburg")
        self.calendar.open()
        self.calendar.set_date(25, 10, 2026)
        self.calendar.set_date(5, 11, 2026)
        self.people.set_people(3, 1)
        self.people.ages(3)
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
        self.calendar.open()
        self.calendar.set_date(10, 7, 2026)
        self.calendar.set_date(5, 8, 2026)
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
        self.calendar.open()
        self.calendar.set_date(10, 7, 2026)
        self.calendar.set_date(15, 7, 2026)
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
        self.calendar.open()
        self.calendar.set_date(25, 9, 2026)
        self.calendar.set_date(5, 10, 2026)
        self.people.set_people(2, 2)
        self.people.ages(5, 12)
        self.stays_page.click_search()
        self.stays_page.cancel_registration_window()
        self.stays_page.proof_location("Germany")

    # @pytest.mark.negative
    # @pytest.mark.regression
    # def test_search_date_in_the_past(self):
    #     self.stays_page.open()
    #     self.stays_page.cancel_registration_window()
    #     self.stays_page.accept_cookies()
    #     self.stays_page.add_destination("Paris")
    #     self.calendar.open()
    #     self.calendar.set_date(8, 6, 2025)
    #     self.calendar.set_date(15, 6, 2025)
    #     self.people.set_people(2, 3)
    #     self.people.ages(0, 8, 17)
    #     self.stays_page.click_search()
    #     self.stays_page.proof_location("Paris")
    #     # TODO:
    #     #  Починить тест, привязав сообщение об установке даты в прошлом

    @pytest.mark.regression
    def test_search_no_dates(self):
        self.stays_page.open()
        self.stays_page.cancel_registration_window()
        self.stays_page.accept_cookies()
        self.stays_page.add_destination("London")
        self.stays_page.click_search()
        self.stays_page.proof_location("London")

    @pytest.mark.negative
    @pytest.mark.regression
    def test_destination_empty(self):
        self.stays_page.open()
        self.stays_page.cancel_registration_window()
        self.stays_page.accept_cookies()
        self.calendar.open()
        self.calendar.set_date(21, 9, 2026)
        self.calendar.set_date(22, 9, 2026)
        self.stays_page.click_search()
        self.stays_page.proof_destination_empty()

    def test_no_properties_found(self):
        self.stays_page.open()
        self.stays_page.accept_cookies()
        self.stays_page.add_non_existent_place("Отель в центре Земли")
        self.stays_page.cancel_registration_window()
        self.calendar.open()
        self.calendar.set_date(23, 9, 2026)
        self.calendar.set_date(30, 9, 2026)
        self.stays_page.click_search()
        self.stays_page.no_property_screen()




    # def test_scroll_to_element(self):
    #     self.stays_page.open()
    #     self.ui.scroll_to(("xpath", "//button[@id='CITY-tab-trigger']"))
    #     time.sleep(3)


