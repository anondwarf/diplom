"""
This module provides the Register class for handling user registration via API.
Classes:
    Register: A class to handle user registration requests to the API.
Usage example:
    register = Register()
    response = register.register_new_user
"""

from utils.http.client import ApiClient
from utils.helpers import environment
from utils.enums import ApiHands, HttpMethods
from utils.helpers import random_user, delete_key_json


class Register(ApiClient):
    """
    A class to handle user registration via API.
    Attributes:
        _url (str): The URL for the registration endpoint.
        _method (str): The HTTP method to be used for the request.
        _payload (dict[str, str] | None): The payload for the registration request.
        _token (str | None): The access token retrieved from the payload.
    Methods:
        _check_payload(): Ensures the payload is set, generates a random user if not provided.
        _get_token(): Retrieves the access token from the payload.
        register_new_user: Registers a new user with the provided or generated payload.
        register_existing_user: Registers an existing user using predefined user data.
        register_user_bad_payload(param: str): Registers a user with a bad payload by removing a specified parameter.
        token: Retrieves the access token, generating it if necessary.
    """

    def __init__(self, payload: dict[str, str] | None = None):
        self._url = environment.BASE_URL + ApiHands.AUTH_REGISTER
        self._method = HttpMethods.POST
        self._payload = payload
        self._token = None
        self._check_payload()

    def _check_payload(self):
        if not self._payload:
            self._payload = random_user()

    def _get_token(self):
        self._token = self._payload.get("accessToken") # type: ignore

    @property
    def register_new_user(self):
        return self.custom_requests(method=self._method, url=self._url, payload=self._payload)

    @property
    def register_existing_user(self):
        return self.custom_requests(method=self._method, url=self._url, payload=environment.user)

    def register_user_bad_payload(self, param: str):
        user = random_user()
        bad_user = delete_key_json(user, param)

        return self.custom_requests(method=self._method, url=self._url, payload=bad_user)

    @property
    def token(self):
        if not self._token:
            self._get_token()
        return self._token
