from random import choices
from string import ascii_letters


def random_string(length: int = 10) -> str:
    return "".join(choices(ascii_letters, k=length))


def random_email(length: int = 10) -> str:
    return random_string(length) + "@mail.com"


def random_user(length: int = 10) -> dict[str, str]:
    return {
        "email": random_email(length),
        "password": random_string(length),
        "name": random_string(length),
    }