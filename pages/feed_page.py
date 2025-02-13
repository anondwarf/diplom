import allure
from selenium.webdriver.common.by import By
from core import BasePage
from core.base_page import WebDriver
from utils.enums import WebLink
from utils import create_order


class _Locators(object):
    FIRST_ORDER = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    FIRST_ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'text_type_digits')]")
    COMPLETED_ORDER_ALL = (By.XPATH, "//p[contains(@class, 'text_type_digits-large')]")
    OPEN_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    CREATED_ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'OrderFeed_number')]")
    IN_WORK_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")

    @staticmethod
    def dynamic_order_number(order_number: str) -> tuple[str, str]:
        return (By.XPATH, f"//p[text()='{order_number}']")

    @staticmethod
    def dynamic_order_number_in_work(order_number: str) -> tuple[str, str]:
        return (By.XPATH, f"//ul/li[text()='{order_number}']")


class FeedPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.page_url = str(WebLink.FEED)
        self._order_number: str | None = None

    @property
    def get_first_order_number(self) -> str:
        with allure.step("Get first order number"):
            self._order_number = self.get_text(_Locators.FIRST_ORDER_NUMBER)
            return self._order_number

    @property
    def open_details_first_order(self) -> None:
        with allure.step("Open details first order"):
            return self.click(_Locators.FIRST_ORDER)

    @property
    def check_order_number_in_modal(self) -> bool:
        with allure.step("Check order number in modal"):
            return self.is_text_present(_Locators.FIRST_ORDER_NUMBER, str(self._order_number))

    @property
    def is_modal_order_open(self) -> bool:
        with allure.step("Check modal order open"):
            return self.is_element_present(_Locators.OPEN_MODAL)

    @property
    def is_created_order_visible(self) -> bool:
        with allure.step("Check created order visible"):
            order_num = str(create_order())
            return self.is_text_present(_Locators.dynamic_order_number(order_num), order_num)

    @property
    def total_orders(self) -> int:
        with allure.step("Get total orders"):
            return int(self.get_text(_Locators.COMPLETED_ORDER_ALL))

    @property
    def is_order_in_work(self) -> bool:
        with allure.step("Check order in work"):
            order_num = str(create_order())
            return self.is_text_present(_Locators.dynamic_order_number_in_work(order_num), order_num)
