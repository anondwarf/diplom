import allure
import json
from utils.helpers import environment


def generate_headers(token: str) -> dict[str, str]:
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    allure.dynamic.parameter(name="headers", value=headers)
    return headers


def delete_key_json(data: dict[str, str], param: str) -> dict[str, str]:
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
        file.seek(0)
        json.dump(json_data, file)
        file.truncate()