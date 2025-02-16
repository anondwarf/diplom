import pytest
from api.auth.user import User
from utils.enums import HttpCodes
from utils.helpers.help_func import generate_headers

@pytest.fixture
def delete_user(request, response):

    token = response.json().get("accessToken")
    headers = generate_headers(token)
    user = User(headers=headers)

    yield

    res = user.delete_user()
    assert res.status_code == HttpCodes.ACCEPTED
