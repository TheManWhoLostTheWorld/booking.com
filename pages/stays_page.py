from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class StaysPage(BasePage):

    _DESTANATION = "//input[@placeholder='Where are you going?']"

    def click_stays(self):
        self.wait.until(EC.element_to_be_clickable(self._STAYS)).click()
        self.wait.until(EC.visibility_of_element_located(self._DESTANATION))