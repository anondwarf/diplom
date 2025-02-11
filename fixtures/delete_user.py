import pytest
from api.auth.user import User
from utils.enums import HttpCodes
from utils.helpers.help_func import generate_headers

@pytest.fixture
def delete_user(request):

    def _delete_user(response):
        token = response.json().get("accessToken")
        headers = generate_headers(token)
        res = User(headers=headers).delete_user
        assert res.status_code == HttpCodes.ACCEPTED

    return _delete_user
