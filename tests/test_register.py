"""
This module contains tests for the user registration functionality of the API.
Tests included:
- test_register_new_uniq_user: Tests the registration of a new unique user.
- test_register_existing_user: Tests the registration of an already existing user.
- test_register_bad_payload: Tests the registration with invalid payloads using parameterized inputs.
Fixtures used:
- delete_user: A fixture to delete a user after registration tests.
Dependencies:
- pytest: For running the tests.
- Register: The registration client from the api.auth module.
- delete_user: A fixture from the fixtures.delete_user module.
- HttpCodes: Enum for HTTP status codes from the utils.enums module.
"""

import pytest
from api.auth import Register
from utils.enums import HttpCodes

def test_register_new_uniq_user(delete_user: dict[str, str]):
    """
    Test the registration of a new unique user.
    This test case verifies that a new user can be registered successfully
    and that the response status code is OK. It also extracts the access token
    from the response and updates the delete_user fixture with the authorization
    headers.
    Args:
        delete_user (fixture): A fixture that handles the deletion of the user
                               after the test is completed.
    """

    reg_client = Register()
    response = reg_client.register_new_user

    assert response.status_code == HttpCodes.OK

    token = response.json().get("accessToken")
    headers = {"Authorization": f"{token}"}
    delete_user.update(headers)


def test_register_existing_user():
    """
    Test case for registering an existing user.
    This test verifies that attempting to register a user who already exists
    in the system results in a forbidden status code.
    Steps:
    1. Create an instance of the Register client.
    2. Attempt to register an existing user.
    3. Assert that the response status code is HttpCodes.FORBIDDEN.
    Expected Result:
    The response status code should be HttpCodes.FORBIDDEN, indicating that
    the registration of an existing user is not allowed.
    """

    reg_client = Register()
    response = reg_client.register_existing_user

    assert response.status_code == HttpCodes.FORBIDDEN


@pytest.mark.parametrize("param", ["email", "password", "name"])
def test_register_bad_payload(param: str):
    """
    Test the registration process with a bad payload.
    This test case verifies that the registration process returns a
    FORBIDDEN status code when provided with an invalid payload.
    Args:
        param: The invalid payload to be tested.
    Asserts:
        The response status code is HttpCodes.FORBIDDEN.
    """

    reg_client = Register()
    response = reg_client.register_user_bad_payload(param)

    assert response.status_code == HttpCodes.FORBIDDEN
