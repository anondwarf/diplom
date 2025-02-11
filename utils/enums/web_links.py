from enum import Enum
from utils import environment


class WebLink(str, Enum):

    FORGOT_PASSWORD = "/forgot-password"
    LOGIN = "/login"
    RESET_PASSWORD = "/reset-password"

    def __str__(self) -> str:
        return environment.BASE_URL + self.value
