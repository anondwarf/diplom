from core import BaseTest


class TestForgotPasswordPage(BaseTest):

    def test_redirect_to_forgot_password(self):
        self.login_page.open()
        self.login_page.click_forgot_password_link()
        assert self.forgot_password_page.is_opened == True