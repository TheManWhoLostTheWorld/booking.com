from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from metaclasses.meta_lacator import MetaLocator
import time


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
        time.sleep(1)
        assert self.wait.until(EC.visibility_of_element_located(self._LOGO))

    def click_logo(self):
        self.wait.until(EC.visibility_of_element_located(self._LOGO)).click()

    def accept_cookies(self):

        try:
            self.driver.find_element(*self._ACCEPT_COOKIES_BUTTON).is_displayed()
            self.wait.until(EC.element_to_be_clickable(self._ACCEPT_COOKIES_BUTTON)).click()
        except NoSuchElementException:
            pass




