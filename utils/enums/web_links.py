from enum import Enum


class WebLink(str, Enum):

    FORGOT_PASSWORD = "/forgot-password"
    LOGIN = "/login"

    def __str__(self):
        return self.value
