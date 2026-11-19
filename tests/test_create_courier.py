import pytest
import requests
import allure
from data import Urls
from helpers import generate_courier_payload


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, courier_data):
        response = requests.post(Urls.CREATE_COURIER, json=courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_error(self, created_courier):
        response = requests.post(Urls.CREATE_COURIER, json=created_courier)

        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json().get("message", "")

    @allure.title("Нельзя создать курьера с уже существующим логином")
    def test_create_courier_existing_login_error(self, created_courier):
        new_payload = generate_courier_payload()
        new_payload["login"] = created_courier["login"]

        response = requests.post(Urls.CREATE_COURIER, json=new_payload)

        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json().get("message", "")

    @allure.title("Ошибка при создании курьера без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field_error(self, missing_field):
        payload = generate_courier_payload()
        del payload[missing_field]

        response = requests.post(Urls.CREATE_COURIER, json=payload)

        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.json().get("message", "")