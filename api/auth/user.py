from utils.http.client import ApiClient
from utils.enums import ApiHands
from utils.enums import HttpMethods
from utils.helpers import environment, change_payload
from api.auth import Login


class User(ApiClient):

    def __init__(self, headers: dict[str, str] | None = None):
        self._url = environment.BASE_URL + ApiHands.AUTH_USER
        self._headers = headers

    def _check_headers(self):
        if not self._headers:
            raise ValueError("Headers are not set")

    @property
    def headers(self):
        return self._headers


    @property
    def delete_user(self):
        self._check_headers()

        return self.custom_requests(url=self._url, method=HttpMethods.DELETE, headers=self._headers)

    def patch_user(self, param: str):
        if self._headers is None:
            self._headers = Login.headers

        user = environment.user
        payload = {
            "user": change_payload(user, param)
        }

        return self.custom_requests(url=self._url, method=HttpMethods.PATCH, headers=self._headers, data=payload)
