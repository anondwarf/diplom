from utils.http.client import ApiClient
from utils.helpers import environment
from utils.enums.api_hands import ApiHands
from utils.enums.http_methods import HttpMethods
from utils.helpers import random_user, change_payload, generate_headers


class Login(ApiClient):

    def __init__(self, payload: dict[str, str] | None = None):
        self._url = environment.BASE_URL + ApiHands.AUTH_LOGIN
        self._method = HttpMethods.POST
        self._payload = payload
        self._headers = None
        self._check_payload()

    def _check_payload(self):
        if self._payload is None:
            user = environment.user
            self._payload = change_payload(user, "name")

    @property
    def login_existing_user(self):
        return self.custom_requests(method=self._method, url=self._url, payload=self._payload)

    @property
    def login_non_existing_user(self):
        user = random_user()
        payload = change_payload(user, "name")

        return self.custom_requests(method=self._method, url=self._url, payload=payload)

    @property
    def headers(self):
        if self._headers is None:
            response = self.login_existing_user.json()
            self._headers = generate_headers(response.get["accessToken"])
        return self._headers