import allure
from selenium.webdriver.common.by import By
from core import BasePage
from core.base_page import WebDriver
from utils.enums import WebLink


class _Locators(object):

    INPUT_HIDE_ICON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    INPUT_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")


class ResetPassword(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.page_url = str(WebLink.RESET_PASSWORD)

    @allure.step("Click hide icon")
    def click_hide_icon(self) -> None:
        self.click(locator=_Locators.INPUT_HIDE_ICON)

    @property
    def is_active_input_password(self) -> bool:
        with allure.step("Check active input password"):
            return self.is_element_present(locator=_Locators.INPUT_ACTIVE)
