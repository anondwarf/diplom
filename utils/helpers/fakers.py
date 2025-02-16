import allure
from random import choices, choice
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
    allure.dynamic.parameter(name="Случайный пользователь", value=data)
    return data


def generate_random_list(length: int, data: list[str] | None = None) -> list[str]:
    result_list = []
    for _ in range(length):
        if data is not None:
            result_list.append(choice(data))
        else:
            result_list.append(random_string())
    return result_list