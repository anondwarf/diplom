from requests import Response, request


class ApiClient:

    @staticmethod
    def custom_requests(*args, **kwargs) -> Response:
        return request(*args, **kwargs)
