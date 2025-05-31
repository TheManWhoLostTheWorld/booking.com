

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from metaclasses.meta_lacator import MetaLocator


class BasePage(metaclass=MetaLocator):

    _ACCEPT_COOKIES_BUTTON = "//button[@id='onetrust-accept-btn-handler']"
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

    def accept_cookies(self):
        self.wait.until(EC.element_to_be_clickable(self._ACCEPT_COOKIES_BUTTON)).click()
        # TODO need to fix a bug with cookies acceptance while opening page first time
        #  sometimes there is no cookies window so tests fail

