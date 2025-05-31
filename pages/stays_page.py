from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class StaysPage(BasePage):

    _STAYS_URL = "https://www.booking.com/index"
    _DESTINATION = "//input[@placeholder='Where are you going?']"
    _CHECK_IN_DATE = "//span[@data-testid='date-display-field-start']"
    _CHECK_OUT_DATE = "//span[@data-testid='date-display-field-end']"
    _SEARCH_BUTTON = "//button[@type='submit']"
    _PEOPLE_SELECT_TRIGGER = "//button[@data-testid='occupancy-config']"


    def click_stays(self):
        self.wait.until(EC.element_to_be_clickable(self._STAYS)).click()
        self.wait.until(EC.visibility_of_element_located(self._DESTINATION))
        assert self._STAYS_URL in self.driver.current_url, "Wrong Stays page URL"

    def add_destination(self, where_to_go):
        self.wait.until(EC.visibility_of_element_located(self._DESTINATION)).send_keys(where_to_go)

    def open_select_people_popup(self):
        self.wait.until(EC.visibility_of_element_located(self._PEOPLE_SELECT_TRIGGER)).click()

    def click_search(self):
        self.wait.until(EC.element_to_be_clickable(self._SEARCH_BUTTON)).click()

    def prof_location(self, destination: str):
        self.wait.until(EC.visibility_of_element_located(('xpath', f"//div[@data-testid='breadcrumbs']//span[contains(text(), {destination})]")))


