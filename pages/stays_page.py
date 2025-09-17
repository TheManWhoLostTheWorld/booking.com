import time

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class StaysPage(BasePage):

    _STAYS_URL = "https://www.booking.com/index"
    _DESTINATION = "//input[@placeholder='Where are you going?']"
    _CHECK_IN_DATE = "//span[@data-testid='date-display-field-start']"
    _CHECK_OUT_DATE = "//span[@data-testid='date-display-field-end']"
    _SEARCH_BUTTON = "//button[@type='submit']"
    _PEOPLE_SELECT_TRIGGER = "//button[@data-testid='occupancy-config']"
    _DROP_DOWN_MENU = "//div[@data-testid='autocomplete-results-options']"


    def click_stays(self):
        self.wait.until(EC.element_to_be_clickable(self._STAYS)).click()
        self.wait.until(EC.visibility_of_element_located(self._DESTINATION))
        assert self._STAYS_URL in self.driver.current_url, "Wrong Stays page URL"

    def add_destination(self, where_to_go: str):
        self.wait.until(EC.visibility_of_element_located(self._DESTINATION)).send_keys(where_to_go)
        self.wait.until(EC.element_to_be_clickable(('xpath', f"//div[@data-testid='autocomplete-results-options']//div[text()='{where_to_go}']/ancestor::li[@role='option']")))

    def open_select_people_popup(self):
        self.wait.until(EC.visibility_of_element_located(self._PEOPLE_SELECT_TRIGGER)).click()

    def click_search(self):
        self.wait.until(EC.element_to_be_clickable(self._SEARCH_BUTTON)).click()

    def proof_location(self, destination: str):
        self.driver.find_element('xpath', f"//div[@data-testid='breadcrumbs']//span[text()='{destination}']")

    def add_destination_by_dropdown(self, half_destination: str):
        self.wait.until(EC.visibility_of_element_located(self._DESTINATION)).send_keys(half_destination)

    def dropdown_destination_click(self, destination: str):
        self.wait.until(EC.element_to_be_clickable(('xpath', f"//div[@data-testid='autocomplete-results-options']//div[text()='{destination}']/ancestor::li[@role='option']"))).click()

    def add_hotel(self, hotel: str):
        self.wait.until(EC.visibility_of_element_located(self._DESTINATION)).send_keys(hotel)
        self.wait.until(EC.element_to_be_clickable(('xpath', f"//div[@data-testid='autocomplete-result']//div[contains(text(), '{hotel}')]")))

    def proof_hotel(self, hotel: str):
        self.wait.until(EC.visibility_of_element_located(('xpath', f"(//div[@data-testid='property-card-container'])[1]//div[contains(text(), '{hotel}')]")))


