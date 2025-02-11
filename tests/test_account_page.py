from pages import MainPage, LoginPage, AccountPage, OrderHistoryPage
from tests.test_reset_password_page import WebDriver
from utils import environment


class TestAccountPage(object):

    def test_redirect_to_login_page_from_main_page(self, driver: WebDriver) -> None:
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open()
        main_page.click_link_account()
        assert login_page.is_opened

    def test_go_to_order_history(self, driver: WebDriver) -> None:
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        order_history_page = OrderHistoryPage(driver)
        main_page = MainPage(driver)
        login_page.open()
        login_page.enter_email(email=environment.USER_LOGIN)
        login_page.enter_password(password=environment.USER_PASSWORD)
        login_page.click_login_button()
        assert main_page.is_opened
        main_page.click_link_account()
        assert account_page.is_opened
        account_page.go_to_order_history_page()
        assert order_history_page.is_opened

    def test_exit_account(self, driver: WebDriver) -> None:
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        main_page = MainPage(driver)
        login_page.open()
        login_page.enter_email(email=environment.USER_LOGIN)
        login_page.enter_password(password=environment.USER_PASSWORD)
        login_page.click_login_button()
        assert main_page.is_opened
        main_page.click_link_account()
        assert account_page.is_opened
        account_page.click_exit_account()
        assert main_page.is_opened
