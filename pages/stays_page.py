from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class StaysPage(BasePage):

    _STAYS_URL = "https://www.booking.com/index"
    _DESTANATION = "//input[@placeholder='Where are you going?']"
    _CHECK_IN_DATE = "//span[@data-testid='date-display-field-start']"
    _CHECK_OUT_DATE = "//span[@data-testid='date-display-field-end']"



    def click_stays(self):
        self.wait.until(EC.element_to_be_clickable(self._STAYS)).click()
        self.wait.until(EC.visibility_of_element_located(self._DESTANATION))
        assert self._STAYS_URL in self.driver.current_url, "Wrong Stays page URL"

    def select_date_current_month(self):
        ...