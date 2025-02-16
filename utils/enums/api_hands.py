from enum import Enum


class ApiHands(str, Enum):
    AUTH_REGISTER = "/api/auth/register"
    AUTH_LOGIN = "/api/auth/login"
    AUTH_USER = "/api/auth/user"
    ORDERS = "/api/orders"

    def __str__(self) -> str:
        return self.value