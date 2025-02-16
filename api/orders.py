import json

from utils.helpers import environment
from utils.enums import ApiHands, HttpMethods, Ingredient
from utils.helpers import generate_random_list
from utils.http.client import ApiClient


class Orders(ApiClient):

    def __init__(self):
        self._url = environment.BASE_URL + ApiHands.ORDERS
        self._headers = None
        self._payload = None
        self._response = None

    @property
    def response(self):
        return self._response

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        self._payload = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    def generate_random_order_payload(self, length: int = 5) -> None:
        ingredients = [_ for _ in Ingredient]
        order_list = generate_random_list(length, ingredients)
        self._payload = {"ingredients": order_list}

    @property
    def post_order(self):
        self._response = self.custom_requests(method=HttpMethods.POST, url=self._url, headers=self._headers, data=json.dumps(self._payload))
        return self._response

    @property
    def get_orders(self):
        self._response = self.custom_requests(method=HttpMethods.GET, url=self._url, headers=self._headers)
        return self._response