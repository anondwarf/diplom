from selenium.webdriver.chrome.webdriver import WebDriver
from pages import LoginPage, ForgotPasswordPage, ResetPassword


class TestResetPasswordPage(object):

    def test_redirect_to_page(self, driver: WebDriver) -> None:
        forgot_password_page = ForgotPasswordPage(driver=driver)
        login_page = LoginPage(driver=driver)
        login_page.open()
        login_page.click_forgot_password_link()
        assert forgot_password_page.is_opened

    def test_enter_email_reset(self, driver: WebDriver) -> None:
        forgot_password_page = ForgotPasswordPage(driver=driver)
        reset_password_page = ResetPassword(driver=driver)
        forgot_password_page.open()
        forgot_password_page.input_email(email="email@email.ru")
        forgot_password_page.click_restore_button()
        assert reset_password_page.is_opened

    def test_active_input_password(self, driver: WebDriver) -> None:
        forgot_password_page = ForgotPasswordPage(driver=driver)
        reset_password_page = ResetPassword(driver=driver)
        forgot_password_page.open()
        forgot_password_page.input_email(email="email@email.ru")
        forgot_password_page.click_restore_button()
        reset_password_page.click_hide_icon()
        assert reset_password_page.is_active_input_password
