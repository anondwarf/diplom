"""
This module contains tests for the login functionality of the application.
Tests:
- test_login_existing_user: Verifies that an existing user can log in successfully.
- test_login_non_existing_user: Verifies that a non-existing user cannot log in and
  receives an unauthorized status code.
"""

from api.auth import Login
from utils.enums import HttpCodes


def test_login_existing_user():
    """
    Test the login functionality for an existing user.
    This test creates an instance of the Login client and attempts to log in
    with an existing user's credentials. It then asserts that the response
    status code is equal to the expected HTTP OK status code.
    Raises:
        AssertionError: If the response status code is not HttpCodes.OK.
    """

    login_client = Login()
    response = login_client.login_existing_user

    assert response.status_code == HttpCodes.OK


def test_login_non_existing_user():
    """
    Test the login functionality with a non-existing user.
    This test case attempts to log in with a user that does not exist in the system.
    It verifies that the response status code is UNAUTHORIZED, indicating that the
    login attempt was unsuccessful due to invalid credentials.
    """

    login_client = Login()
    response = login_client.login_non_existing_user

    assert response.status_code == HttpCodes.UNAUTHORIZED
