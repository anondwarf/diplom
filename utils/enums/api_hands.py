from enum import Enum


class ApiHands(str, Enum):
    AUTH_REGISTER = "/api/auth/register"
    AUTH_USER = "/api/auth/login"

    def __str__(self) -> str:
        return self.value