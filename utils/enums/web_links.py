from enum import Enum
from utils import environment


class WebLink(str, Enum):

    FORGOT_PASSWORD = "/forgot-password"
    LOGIN = "/login"
    RESET_PASSWORD = "/reset-password"
    ACCOUNT_PROFILE = "/account/profile"
    ACCOUNT_ORDER_HISTORY = "/account/order-history"
    FEED = "/feed"

    def __str__(self) -> str:
        return environment.BASE_URL + self.value
