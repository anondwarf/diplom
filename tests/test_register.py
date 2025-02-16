import allure
import pytest
from api.auth import Register
from utils.enums import HttpCodes


@allure.suite("Регистрация пользователя")
class TestRegister:

    @allure.title("Проверка регистрации уникального пользователя")
    def test_new_uniq_user(self, delete_user):
        reg_client = Register()
        response = reg_client.register_new_user
        assert response.status_code == HttpCodes.OK
        assert response.json()["success"]
        delete_user(response)

    @allure.title("Проверка регистрации существующего пользователя")
    def test_existing_user(self):
        reg_client = Register()
        response = reg_client.register_existing_user
        assert response.status_code == HttpCodes.FORBIDDEN
        assert not response.json()["success"]

    @pytest.mark.parametrize("param", ["email", "password", "name"])
    @allure.title("Проверка регистрации пользователя, без ключа {param}")
    def test_bad_payload(self, param: str):
        reg_client = Register()
        response = reg_client.register_user_bad_payload(param)
        assert response.status_code == HttpCodes.FORBIDDEN
        assert not response.json()["success"]
