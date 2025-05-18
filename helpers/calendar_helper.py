from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_page import BasePage

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

class CalendarHelper(BasePage):

    _CALENDAR_TABLE = "//span[contains(text(), 'Calendar')]"
    _FLEXIBLE_TABLE = "//span[contains(text(), 'flexible')]"
    _CALENDAR_TRIGGER_BUTTON = "//span[@data-testid='date-display-field-start']"
    _CALENDAR = "//div[@id='calendar-searchboxdatepicker']"
    _CURRENT_MONTHS_AND_YEAR = ".//h3[1]"
    _NEXT_MONTHS_BUTTON = "//button[@aria-label='Next month']"
    _PREVIOUS_MONTH_BUTTON = "//button[@aria-label='Previous month']"
    _DAY = ".//table//td[.//span]"
    _DAY_STATUS = ".//span"
    _PLUS_MINUS_DAYS = "//div[@data-testid='flexible-dates-container']//label[.//input]"
    _PLUS_MINUS_DAYS_STATUS = ".//input"


    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, 1)

    def open(self):
        self.wait.until(EC.element_to_be_clickable(self._CALENDAR_TRIGGER_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self._CALENDAR), message="Calendar was not opened")

    def click_next_month_button(self):
        calendar = self.wait.until(EC.visibility_of_element_located(self._CALENDAR))
        calendar.find_element(*self._NEXT_MONTHS_BUTTON).click()

    def set_date(self, day: int, month: int, year: int):
        target_month_year = f"{months[month]} {year}"
        calendar = self.wait.until(EC.visibility_of_element_located(self._CALENDAR))
        while target_month_year not in self.driver.find_element(*self._CURRENT_MONTHS_AND_YEAR).text:
            self.click_next_month_button()
            time.sleep(0.5)
        days = calendar.find_elements(*self._DAY)
        for element in days:
            if str(day) in element.text:
                element.click()
                # assert element.find_element(*self._DAY_STATUS).get_attribute("aria_checked") == "true"
                # break

    def plus_minus_day(self, days: int):
        elements = self.wait.until(EC.visibility_of_all_elements_located(self._PLUS_MINUS_DAYS))
        for element in elements:
            if str(days) in element.text:
                element.click()
                assert element.find_element(*self._PLUS_MINUS_DAYS).is_selected()
                break












