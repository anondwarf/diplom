import allure
from api.auth import Login
from utils.enums import HttpCodes


@allure.suite("Авторизация")
class TestLogin:

    @allure.title("Проверка авторизации существующего пользователя")
    def test_existing_user(self):
        login_client = Login()
        response = login_client.login_existing_user
        assert response.status_code == HttpCodes.OK
        assert response.json()["success"]

    @allure.title("Проверка авторизации не существующего пользователя")
    def test_non_existing_user(self):
        login_client = Login()
        response = login_client.login_non_existing_user
        assert response.status_code == HttpCodes.UNAUTHORIZED
        assert not response.json()["success"]
