from base.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckBoxHelper(BasePage):

    _BREAKFAST_INCLUDED_CB = "//div[@data-filters-group='mealplan']//input[contains(@aria-label, 'Breakfast included')]"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, 1)

    def click_breakfast_included_cb(self):
        checkbox = self.driver.find_element(*self._BREAKFAST_INCLUDED_CB)
        checkbox.click()
        assert checkbox.is_selected()
        # TODO
        #  1. scroll to element (checkbox)
        #  2. all checkboxes


