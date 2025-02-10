"""
This module provides the Login class for handling user authentication via API requests.
Classes:
    Login: A class to manage login operations for existing and non-existing users.
Usage:
    - Instantiate the Login class with an optional payload.
    - Use the login_existing_user property to log in with an existing user.
    - Use the login_non_existing_user property to log in with a non-existing user.
    - Use the headers property to get the headers with the access token after logging in.
Dependencies:
    - utils.http.client.ApiClient
    - utils.helpers.environment
    - utils.enums.api_hands.ApiHands
    - utils.enums.http_methods.HttpMethods
    - utils.helpers.random_user
    - utils.helpers.delete_key_json
    - utils.helpers.generate_headers
"""

from utils.http.client import ApiClient
from utils.helpers import environment
from utils.enums.api_hands import ApiHands
from utils.enums.http_methods import HttpMethods
from utils.helpers import random_user, delete_key_json, generate_headers


class Login(ApiClient):
    """
    A class to handle user login operations using the ApiClient.
    Attributes:
        _url (str): The URL for the login endpoint.
        _method (str): The HTTP method to be used for the login request.
        _payload (dict[str, str] | None): The payload for the login request.
        _headers (dict[str, str] | None): The headers for the login request.
    Methods:
        __init__(payload: dict[str, str] | None = None):
            Initializes the Login instance with the given payload.
        _check_payload():
            Checks and sets the payload if it is None.
        login_existing_user():
            Logs in an existing user and returns the response.
        login_non_existing_user():
            Logs in a non-existing user and returns the response.
        headers():
            Generates and returns the headers using the access token from the login response.
    """

    def __init__(self, payload: dict[str, str] | None = None):
        self._url = environment.BASE_URL + ApiHands.AUTH_LOGIN
        self._method = HttpMethods.POST
        self._payload = payload
        self._headers = None
        self._check_payload()

    def _check_payload(self):
        if self._payload is None:
            user = environment.user
            self._payload = delete_key_json(user, "name") # type: ignore

    @property
    def login_existing_user(self):
        return self.custom_requests(method=self._method, url=self._url, payload=self._payload)

    @property
    def login_non_existing_user(self):
        user = random_user()
        payload = delete_key_json(user, "name")

        return self.custom_requests(method=self._method, url=self._url, payload=payload)

    @property
    def headers(self):
        response = self.login_existing_user.json()
        self._headers = generate_headers(response.get("accessToken"))
        return self._headers
