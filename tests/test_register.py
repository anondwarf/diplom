import pytest
from api.auth import Register
from utils.enums import HttpCodes

def test_register_new_uniq_user(delete_user):
    reg_client = Register()
    response = reg_client.register_new_user

    assert response.status_code == HttpCodes.OK

    delete_user(response)


def test_register_existing_user():
    reg_client = Register()
    response = reg_client.register_existing_user

    assert response.status_code == HttpCodes.FORBIDDEN


@pytest.mark.parametrize("param", ["email", "password", "name"])
def test_register_bad_payload(param: str):
    reg_client = Register()
    response = reg_client.register_user_bad_payload(param)

    assert response.status_code == HttpCodes.FORBIDDEN
