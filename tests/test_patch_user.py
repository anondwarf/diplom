import pytest
from api.auth import User
from utils.enums import HttpCodes
from utils.helpers import write_user_change


@pytest.mark.parametrize("param", ["name", "email", "password"])
def test_patch_user_with_auth(param):
    patch_client = User()

    response = patch_client.patch_user(param)

    assert response.status_code == HttpCodes.OK

    write_user_change(response.json(), param)
    
    # todo доделать

