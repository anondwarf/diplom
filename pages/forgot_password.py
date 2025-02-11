from core import BasePage
from utils.enums import WebLink


class _Locators(object): ...


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = WebLink.FORGOT_PASSWORD
