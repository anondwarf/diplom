import allure
from core import BasePage
from utils.enums import WebLink
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class _Locators(object):

    INPUT_EMAIL = (By.XPATH, "//input[@name='name']")
    BUTTON_RESET_PASSWORD = (By.XPATH, "//button[contains(text(), 'Восстановить')]")


class ForgotPasswordPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.page_url = str(WebLink.FORGOT_PASSWORD)

    @allure.step("Input email")
    def input_email(self, email: str) -> None:
        self.input_text(locator=_Locators.INPUT_EMAIL, text=email)

    @allure.step("Click restore button")
    def click_restore_button(self) -> None:
        self.click(locator=_Locators.BUTTON_RESET_PASSWORD)
