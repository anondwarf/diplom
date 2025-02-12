import json
import requests
from utils import environment


def _auth_user_api():
    url = environment.BASE_URL + "/api/auth/login"
    login = environment.USER_LOGIN
    password = environment.USER_PASSWORD
    response = requests.post(url, json={"email": login, "password": password})
    token = response.json().get("accessToken")
    return token


def create_order():
    url = environment.BASE_URL + "/api/orders"
    ingredients = ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa71"]
    token = _auth_user_api()
    headers = {"Authorization": f"{token}", "Content-Type": "application/json"}

    response = requests.post(url=url, headers=headers, data=json.dumps({"ingredients": ingredients}))
    order_data = response.json().get("order")
    print(order_data)
    if order_data is None:
        raise ValueError("Order creation failed, 'order' key not found in response")
    order_number = order_data.get("number")
    return order_number
