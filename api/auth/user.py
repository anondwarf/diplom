"""
This module provides the User class for interacting with the user-related API endpoints.
Classes:
    User: A class to handle user-related API operations such as deleting and patching user information.
Usage example:
    user = User(headers={"Authorization": "Bearer token"})
    response = user.delete_user
    response = user.patch_user("email")
"""

from utils.http.client import ApiClient
from utils.enums import ApiHands
from utils.enums import HttpMethods
from utils.helpers import environment, random_string, random_email
from api.auth import Login


class User(ApiClient):
    """
    A class to represent a user and perform various user-related operations.
    Attributes:
    -----------
    _url : str
        The base URL for user-related API endpoints.
    _headers : dict[str, str] | None
        The headers to be used in the API requests.
    Methods:
    --------
    _check_headers():
        Checks if headers are set, raises ValueError if not.
    delete_user:
        Deletes the user using the DELETE HTTP method.
    patch_user(param: str):
        Updates the user information based on the provided parameter using the PATCH HTTP method.
    """

    def __init__(self, headers: dict[str, str] | None = None):
        self._url = environment.BASE_URL + ApiHands.AUTH_USER
        self._headers = headers

    def _check_headers(self):
        if not self._headers:
            raise ValueError("Headers are not set")

    @property
    def delete_user(self):
        self._check_headers()

        return self.custom_requests(url=self._url, method=HttpMethods.DELETE, headers=self._headers)

    def patch_user(self, param: str):
        self._headers = Login().headers

        if param == "email":
            payload = {"user": { param: random_email()}}
        if param in ["password", "name"]:
            payload = {"user": { param: random_string()}}

        return self.custom_requests(url=self._url, method=HttpMethods.PATCH, headers=self._headers, data=payload)
