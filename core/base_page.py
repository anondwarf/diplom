import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.page_url = None
        self.wait = WebDriverWait(self.driver, 10, 1)

    def open(self):
        with allure.step(f"Open page {self.page_url}"):
            self.driver.get(self.page_url)

    @property
    def is_opened(self):
        return self.wait.until(EC.url_contains(self.page_url))

    def click(self, locator):
        with allure.step(f"Click page {locator}"):
            self.wait.until(EC.presence_of_element_located(locator)).click()