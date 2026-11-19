import requests
import allure
from data import Urls


class TestGetOrdersList:

    @allure.title("Получение списка заказов")
    def test_get_orders_list_returns_list(self):
        response = requests.get(Urls.ORDERS)
        response_json = response.json()

        assert response.status_code == 200
        assert "orders" in response_json
        assert isinstance(response_json["orders"], list)