from core import BasePage
from utils.enums import WebLink
from selenium.webdriver.remote.webdriver import WebDriver


class _Locators(object):

    FORGOT_PASSWORD_LINK = ("xpath", "//a[@href='/forgot-password']")


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.page_url = str(WebLink.LOGIN)

    def click_forgot_password_link(self) -> None:
        self.click(locator=_Locators.FORGOT_PASSWORD_LINK)
