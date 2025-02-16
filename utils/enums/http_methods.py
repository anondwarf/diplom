from enum import Enum


class HttpMethods(str, Enum):
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"
    GET = "GET"

    def __str__(self) -> str:
        return self.value