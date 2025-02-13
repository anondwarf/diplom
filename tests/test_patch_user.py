import allure
import pytest
from api.auth import User, Login
from utils.enums import HttpCodes
from utils.helpers import write_user_change


@allure.suite("Изменение пользователя")
class TestPatchUser:

    @pytest.mark.parametrize("param", ["email", "name", "password"])
    @allure.title("Проверка изменения у пользователя {param}")
    def test_patch_user_with_auth(self, auth_headers, param, request):
        patch_client = User(headers=auth_headers)
        response = patch_client.patch_user(param)
        assert response.status_code == HttpCodes.OK
        assert response.json()["success"]
        login_client = Login(patch_client.payload)
        response = login_client.login
        assert response.status_code == HttpCodes.OK
        assert response.json()["success"]
        write_user_change(patch_client.payload, request.param)
