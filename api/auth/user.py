from utils.http.client import ApiClient
from utils.helpers import environment
from utils.enums import ApiHands
from utils.enums import HttpMethods


class User(ApiClient):

    def __init__(self, headers: dict[str, str] | None = None):
        self._url = environment.BASE_URL + ApiHands.AUTH_LOGIN
        self._headers = headers

    def _check_headers(self):
        if not self._headers:
            raise ValueError("Headers are not set")

    @property
    def delete_user(self):
        return self.custom_requests(url=self._url, method=HttpMethods.DELETE, headers=self._headers)
