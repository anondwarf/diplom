from selenium.webdriver.common.by import By
from core import BasePage
from core.base_page import WebDriver
from utils import environment


class _Locator(object):

    LINK_ACCOUNT = (By.XPATH, "//a[@href='/account']")
    LINK_FEED = (By.XPATH, "//a[@href='/feed']")


class MainPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.page_url = str(environment.BASE_URL)

    def click_link_account(self) -> None:
        self.click(locator=_Locator.LINK_ACCOUNT)

    def got_to_feed_page(self) -> None:
        self.click(locator=_Locator.LINK_FEED)
