import time

from base.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class PeopleHelper(BasePage):

    _PEOPLE_SELECT_TRIGGER = "//button[@data-testid='occupancy-config']"
    _PEOPLE_SELECT_POPUP = "//div[@data-testid='occupancy-popup']"
    _QTY_ADULTS_INFO = "//div[@data-testid='occupancy-popup']//div[input[@id='group_adults']]//div[2]/span"
    _ADULTS_SELECT_MINUS = "(//div[@data-testid='occupancy-popup']//button)[1]"
    _ADULTS_SELECT_PLUS = "(//div[@data-testid='occupancy-popup']//button)[2]"
    _QTY_CHILDREN_INFO = "//div[@data-testid='occupancy-popup']//div[input[@id='group_children']]//div[2]/span"
    _CHILDREN_SELECT_MINUS = "(//div[@data-testid='occupancy-popup']//button)[3]"
    _CHILDREN_SELECT_PLUS = "(//div[@data-testid='occupancy-popup']//button)[4]"
    _ROOMS_SELECT_MINUS = "(//div[@data-testid='occupancy-popup']//button)[5]"
    _ROOMS_SELECT_PLUS = "(//div[@data-testid='occupancy-popup']//button)[6]"


    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, 1)
        # self.dropdown = Select(self.driver.find_element())


    def open_select_people_popup(self):
        self.wait.until(EC.element_to_be_clickable(self._PEOPLE_SELECT_TRIGGER)).click()
        self.wait.until(EC.visibility_of_element_located(self._PEOPLE_SELECT_POPUP), message="People select popup was not opened")


    def set_people(self, adults, children):

        self.open_select_people_popup()

        while adults != int(self.wait.until(EC.visibility_of_element_located(self._QTY_ADULTS_INFO)).text):
            if adults < int(self.driver.find_element(*self._QTY_ADULTS_INFO).text):
                self.driver.find_element(*self._ADULTS_SELECT_MINUS).click()
            elif adults > int(self.driver.find_element(*self._QTY_ADULTS_INFO).text):
                self.driver.find_element(*self._ADULTS_SELECT_PLUS).click()
        assert adults == int(self.driver.find_element(*self._QTY_ADULTS_INFO).text), "Wrong adults qty"

        while children != int(self.wait.until(EC.visibility_of_element_located(self._QTY_CHILDREN_INFO)).text):
            self.driver.find_element(*self._CHILDREN_SELECT_PLUS).click()
            time.sleep(0.5)
        assert children == int(self.driver.find_element(*self._QTY_CHILDREN_INFO).text), "Wrong children qty"


    def ages(self, *args: int): # 10 args - maximum

        number_of_children = 0
        ages = []
        for child in args:
            ages.append(child)
            number_of_children += 1

        def get_age_xpath(qty_children):
            return f"(//div[@data-testid='kids-ages-select'])[{qty_children}]//select"

        for xpath in range(0, number_of_children):

            dropdown = Select(self.driver.find_element('xpath',get_age_xpath(xpath + 1)))
            dropdown.select_by_value(str(ages[xpath]))
            self.wait.until(EC.element_to_be_clickable(self._PEOPLE_SELECT_TRIGGER)).click()














