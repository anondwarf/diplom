from enum import Enum


class HttpCodes(int, Enum):
    OK = 200
    ACCEPTED = 202
    BAD_REQUEST = 400
    FORBIDDEN = 403

    def __int__(self) -> int:
        return self.value
