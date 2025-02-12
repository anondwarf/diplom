from pages import FeedPage
from pages.account_page import WebDriver
from utils import create_order


class TestFeed(object):

    def test_open_modal_order(self, driver: WebDriver) -> None:
        feed_page = FeedPage(driver)
        feed_page.open()
        feed_page.open_details_first_order
        assert feed_page.is_modal_order_open

    def test_visible_created_order(self, driver: WebDriver) -> None:
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.is_created_order_visible

    def test_increment_total_orders_after_order_creation(self, driver: WebDriver) -> None:
        feed_page = FeedPage(driver)
        feed_page.open()
        total_orders = feed_page.total_orders
        create_order()
        assert feed_page.total_orders == total_orders + 1

    def test_order_in_work_after_creation(self, driver: WebDriver) -> None:
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.is_order_in_work
