import pytest
import requests
import allure
from data import Urls, OrderData


class TestCreateOrder:

    @allure.title("Успешное создание заказа с разными вариантами цвета")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, color):
        payload = OrderData.BASE_ORDER.copy()
        payload["color"] = color

        response = requests.post(Urls.ORDERS, json=payload)
        response_json = response.json()

        assert response.status_code == 201
        assert "track" in response_json and response_json["track"] is not None

        # Удаляем/отменяем созданный заказ после теста
        requests.put(Urls.CANCEL_ORDER, params={"track": response_json["track"]})