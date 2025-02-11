from pages import LoginPage, ForgotPasswordPage


class TestForgotPasswordPage(object):

    def test_redirect_to_forgot_password(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        login_page.open()
        login_page.click_forgot_password_link()
        assert forgot_password_page.is_opened
