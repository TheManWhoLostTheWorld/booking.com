

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from metaclasses.meta_lacator import MetaLocator


class BasePage(metaclass=MetaLocator):

    _PAGE_URL = "https://www.booking.com/"
    _LOGO = "//a[@data-testid='header-booking-logo']"
    _STAYS = "//a[@id='accommodations']"
    _CAR_RENTALS_BUTTON = "//a[@id='cars']"


    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, 1)

    def open(self):
       self.driver.get(self._PAGE_URL)

    def click_logo(self):
        self.wait.until(EC.visibility_of_element_located(self._LOGO)).click()

