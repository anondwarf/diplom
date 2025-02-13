import allure
from selenium.webdriver.common.by import By
from core import BasePage
from utils.enums import WebLink
from selenium.webdriver.remote.webdriver import WebDriver


class _Locators(object):

    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    INPUT_EMAIL = (By.XPATH, "//input[@name='name']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LINK_MAIN_PAGE = (By.XPATH, "//a[@href='/']")


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.page_url = str(WebLink.LOGIN)

    @allure.step("Click forgot password link")
    def click_forgot_password_link(self) -> None:
        self.click(locator=_Locators.FORGOT_PASSWORD_LINK)

    @allure.step("Enter email")
    def enter_email(self, email: str) -> None:
        self.input_text(locator=_Locators.INPUT_EMAIL, text=email)

    @allure.step("Enter password")
    def enter_password(self, password: str) -> None:
        self.input_text(locator=_Locators.INPUT_PASSWORD, text=password)

    @allure.step("Click login button")
    def click_login_button(self) -> None:
        self.click(locator=_Locators.LOGIN_BUTTON)

    @allure.step("Go to main page")
    def go_to_main_page(self) -> None:
        self.click(locator=_Locators.LINK_MAIN_PAGE)
