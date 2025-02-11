import pytest
from api.auth import Login


@pytest.fixture
def auth_headers():
    headers = Login().headers
    return headers
