from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CarRentalsPage(BasePage):

    _CAR_RENTALS_URL = "https://www.booking.com/cars/"

    def open_car_rental_page(self):
        button = self.wait.until(EC.element_to_be_clickable(self._CAR_RENTALS_BUTTON))
        button.click()
        assert self._CAR_RENTALS_URL in self.driver.current_url