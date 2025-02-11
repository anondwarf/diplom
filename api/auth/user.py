import json

from utils.http.client import ApiClient
from utils.enums import ApiHands
from utils.enums import HttpMethods
from utils.helpers import environment, random_string, random_email
from api.auth import Login


class User(ApiClient):

    def __init__(self, headers: dict[str, str] | None = None):
        self._url = environment.BASE_URL + ApiHands.AUTH_USER
        self._headers = headers
        self._payload = None

    def _check_headers(self):
        if not self._headers:
            raise ValueError("Headers are not set")

    @property
    def payload(self):
        return self._payload

    @property
    def delete_user(self):
        self._check_headers()
        return self.custom_requests(url=self._url, method=HttpMethods.DELETE, headers=self._headers)

    def patch_user(self, param: str):
        self._check_headers()
        if param == "email":
            self._payload = {"user": { param: random_email()}}
        if param in ["password", "name"]:
            self._payload = {"user": { param: random_string()}}
        return self.custom_requests(url=self._url, method=HttpMethods.PATCH, headers=self._headers, data=json.dumps(self._payload))
