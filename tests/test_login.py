from api.auth import Login
from utils.enums import HttpCodes


def test_login_existing_user():
    login_client = Login()
    response = login_client.login_existing_user

    assert response.status_code == HttpCodes.OK


def test_login_non_existing_user():
    login_client = Login()
    response = login_client.login_non_existing_user

    assert response.status_code == HttpCodes.UNAUTHORIZED
