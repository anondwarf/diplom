from pages import *
from selenium.webdriver.remote.webdriver import WebDriver


class TestPages(object):

    def test_redirect_to_main_page(self, driver: WebDriver) -> None:
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        login_page.go_to_main_page()
        assert main_page.is_opened

    def test_redirect_to_feed_page(self, driver: WebDriver) -> None:
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.open()
        main_page.got_to_feed_page()
        assert feed_page.is_opened
