from base.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class UiHelper(BasePage):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, 1)
        self.action = ActionChains(self.driver)

    # def find(self, locator):
    #     return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_to(self, locator):
        self.action.scroll_to_element(self.wait.until(EC.visibility_of_element_located(locator)))
        self.driver.execute_script("""window.scrollTo({top: window.scrollY + 500,});""")