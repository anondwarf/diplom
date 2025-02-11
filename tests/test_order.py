import allure
from api import Orders
from utils.enums import HttpCodes
from utils.helpers import generate_random_list


@allure.suite("Заказы")
class TestOrder:

    @allure.title("Создание заказа с авторизацией пользователя и списком ингредиентов")
    def test_with_auth_and_ingredients(self, auth_headers):
        order_client = Orders()
        order_client.headers = auth_headers
        order_client.generate_random_order_payload()
        response = order_client.post_order
        assert response.status_code == HttpCodes.OK

    @allure.title("Создание заказа без авторизации и список ингредиентов")
    def test_with_auth_and_without_ingredients(self, auth_headers):
        order_client = Orders()
        order_client.generate_random_order_payload()
        response = order_client.post_order
        assert response.status_code == HttpCodes.BAD_REQUEST

    @allure.title("Создание заказа с авторизацией и без списка ингредиентов")
    def test_without_auth_and_with_ingredients(self, auth_headers):
        order_client = Orders()
        order_client.headers = auth_headers
        response = order_client.post_order
        assert response.status_code == HttpCodes.BAD_REQUEST

    @allure.title("Создание заказа с авторизацией и не верными хешами ингредиентов")
    def test_with_auth_and_bad_hash_ingredients(self, auth_headers):
        order_client = Orders()
        order_client.headers = auth_headers
        order_client.payload = generate_random_list(5)
        response = order_client.post_order
        assert response.status_code == HttpCodes.BAD_REQUEST

    @allure.title("Получение списка заказов пользователя")
    def test_auth_user(self, auth_headers):
        order_client = Orders()
        order_client.headers = auth_headers
        response = order_client.get_orders
        assert response.status_code == HttpCodes.OK

    @allure.title("Получение списка заказов")
    def test_no_auth_user(self):
        order_client = Orders()
        response = order_client.get_orders
        assert response.status_code == HttpCodes.UNAUTHORIZED