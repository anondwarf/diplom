from core import BasePage
from utils.enums import WebLink


class _Locators(object):

    FORGOT_PASSWORD_LINK = ("xpath", "a[href='/forgot-password']")


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = WebLink.LOGIN

    def click_forgot_password_link(self):
        self.click(locator=_Locators.FORGOT_PASSWORD_LINK)