import allure
from random import choices
from string import ascii_letters


def random_string(length: int = 10) -> str:
    string = "".join(choices(ascii_letters, k=length))
    allure.dynamic.parameter(name="Случайная строка", value=string)
    return string


def random_email(length: int = 10) -> str:
    string = random_string(length) + "@mail.com"
    allure.dynamic.parameter(name="Случайная почта", value=string)
    return string


def random_user(length: int = 10) -> dict[str, str]:
    data = {
        "email": random_email(length),
        "password": random_string(length),
        "name": random_string(length),
    }
    allure.attach(body=data, name="Случайный пользователь", attachment_type=allure.attachment_type.JSON)
    return data