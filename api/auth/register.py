from utils.http.client import ApiClient
from utils.helpers import environment
from utils.enums import ApiHands, HttpMethods
from utils.helpers import random_user, delete_key_json


class Register(ApiClient):

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
        return self.custom_requests(method=self._method, url=self._url, data=self._payload)

    @property
    def register_existing_user(self):
        return self.custom_requests(method=self._method, url=self._url, data=environment.user)

    def register_user_bad_payload(self, param: str):
        user = random_user()
        bad_user = delete_key_json(user, param)

        return self.custom_requests(method=self._method, url=self._url, data=bad_user)

    @property
    def token(self):
        if not self._token:
            self._get_token()
        return self._token
