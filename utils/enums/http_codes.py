from enum import Enum


class HttpCodes(int, Enum):
    OK = 200
    ACCEPTED = 202

    def __int__(self) -> int:
        return self.value
