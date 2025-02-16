from core import BasePage
from core.base_page import WebDriver
from utils.enums import WebLink


class _Locators(object): ...


class OrderHistoryPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.page_url = str(WebLink.ACCOUNT_ORDER_HISTORY)
