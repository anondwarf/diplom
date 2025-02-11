from pages import *
from selenium.webdriver.remote.webdriver import WebDriver

from utils import environment


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

    def test_open_modal_ingredient(self, driver: WebDriver) -> None:
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_fist_ingredient()
        assert main_page.is_modal_present

    def test_close_modal_ingredient(self, driver: WebDriver) -> None:
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_fist_ingredient()
        main_page.close_modal()
        assert main_page.is_modal_not_present

    def test_ingredient_counter(self, driver: WebDriver) -> None:
        main_page = MainPage(driver)
        main_page.open()
        count = main_page.count_ingredients
        main_page.add_first_ingredient_to_constructor()
        new_count = main_page.count_ingredients
        assert new_count == count + 2

    def test_create_order_auth_user(self, driver: WebDriver) -> None:
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        login_page.open()
        login_page.enter_email(email=environment.USER_LOGIN)
        login_page.enter_password(password=environment.USER_PASSWORD)
        login_page.click_login_button()
        main_page.create_order()
        assert main_page.is_order_created

