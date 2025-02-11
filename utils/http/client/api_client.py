import allure
from requests import Response, request


class ApiClient:

    @staticmethod
    def custom_requests(*args, **kwargs) -> Response:
        with allure.step(f"HTTP запрос с параметрами: {args}, {kwargs}"):
            return request(*args, **kwargs)
