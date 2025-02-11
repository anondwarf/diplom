import allure
import json
from utils.helpers import environment


def generate_headers(token: str) -> dict[str, str]:
    headers = {
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
        "Authorization": f"{token}",
        "Content-Type": "application/json",
        "Accept": "*/*"
    }
    allure.dynamic.parameter(name="headers", value=headers)
    return headers


def delete_key_json(data: dict[str, str], param: str) -> dict[str, str]:
    if param in data:
        data.pop(param)
    allure.dynamic.parameter(name="edited data", value=data)
    return data


def change_key_value_json(data: dict[str, str], param: str, new_value: str) -> dict[str, str]:
    data[param] = new_value
    allure.dynamic.parameter(name="edited data", value=data)
    return data


def write_user_change(data: dict[str, str], param: str) -> None:
    new_value = data.get(param)

    with open(environment.USER_FILE, "r+") as file:
        json_data = json.load(file)
        json_data[param] = new_value
        json.dump(json_data, file)
