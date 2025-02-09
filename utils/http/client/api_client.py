from requests import Response, request


class ApiClient:

    @staticmethod
    def custom_requests(method: str, url: str, **kwargs) -> Response:
        if 'payload' in kwargs:
            kwargs['data'] = kwargs.pop('payload')
        return request(method=method, url=url, **kwargs)
