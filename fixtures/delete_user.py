import pytest
from api.auth.user import User
from utils.enums import HttpCodes

@pytest.fixture
def delete_user():
    headers = {}
    yield headers
    response = User(headers=headers).delete_user
    assert response.status_code == HttpCodes.ACCEPTED
