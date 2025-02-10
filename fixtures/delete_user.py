"""
This module contains a pytest fixture for deleting a user.
Fixtures:
    delete_user: A fixture that sets up headers for a user deletion request and
                 asserts that the deletion request returns an accepted status code.
"""

import pytest
from api.auth.user import User
from utils.enums import HttpCodes

@pytest.fixture
def delete_user():
    """
    Deletes a user by sending a DELETE request.

    This function generates the necessary headers, sends a DELETE request
    to delete a user, and asserts that the response status code is HTTP 202 Accepted.

    Yields:
        dict: The headers used for the DELETE request.

    Raises:
        AssertionError: If the response status code is not HTTP 202 Accepted.
    """

    headers = {}
    yield headers
    response = User(headers=headers).delete_user
    assert response.status_code == HttpCodes.ACCEPTED
