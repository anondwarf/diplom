import allure
from core import BasePage
from pages.forgot_password import By
from tests.test_reset_password_page import WebDriver
from utils.enums import WebLink


class _Locators(object):

    LINK_ORDER_HISTORY = (By.XPATH, "//a[@href='/account/order-history']")
    BUTTON_EXIT_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Выход')]")


class AccountPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.page_url = str(WebLink.ACCOUNT_PROFILE)

    @allure.step("Переход на страницу истории заказов")
    def go_to_order_history_page(self) -> None:
        self.click(locator=_Locators.LINK_ORDER_HISTORY)

    @allure.step("Выход из аккаунта")
    def click_exit_account(self) -> None:
        self.click(locator=_Locators.BUTTON_EXIT_ACCOUNT)
