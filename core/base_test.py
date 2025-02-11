import pytest
from pages import LoginPage, ForgotPasswordPage


class BaseTest:

    login_page: LoginPage
    forgot_password_page: ForgotPasswordPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.forgot_password_page = ForgotPasswordPage(driver)