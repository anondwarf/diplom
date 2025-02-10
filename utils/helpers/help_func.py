import json
from utils.helpers import environment


def generate_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"{token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

def delete_key_json(payload: dict[str, str], param: str) -> dict[str, str]:
    payload.pop(param)
    return payload


def change_value_json(payload: dict[str, str], param: str, new_value: str) -> dict[str, str]:
    payload[param] = new_value
    return payload


def write_user_change(data: dict[str, str], param: str) -> None:
    new_value = data.get(param)

    with open(environment.USER_FILE, "r+") as file:
        json_data = json.load(file)
        json_data[param] = new_value
        file.seek(0)
        json.dump(json_data, file)
        file.truncate()
