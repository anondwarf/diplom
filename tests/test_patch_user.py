import allure
import pytest
from api.auth import User
from utils.enums import HttpCodes
from utils.helpers import write_user_change


@allure.suite("Изменение пользователя")
class TestPatchUser:

    @pytest.mark.parametrize("param", ["email", "password"])
    @allure.title("Проверка изменения у пользователя {param}")
    def test_patch_user_with_auth(self, param):
        patch_client = User()
        response = patch_client.patch_user(param)

        assert response.status_code == HttpCodes.OK

        write_user_change(response.json(), param)
