import pytest
import requests
import allure
from data import Urls
from helpers import generate_random_string


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, created_courier):
        payload = {
            "login": created_courier["login"],
            "password": created_courier["password"]
        }
        response = requests.post(Urls.LOGIN_COURIER, json=payload)

        assert response.status_code == 200
        assert "id" in response.json() and response.json()["id"] is not None

    @allure.title("Ошибка при авторизации без обязательного поля (логина или пароля)")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_missing_field_error(self, created_courier, missing_field):
        payload = {
            "login": created_courier["login"],
            "password": created_courier["password"]
        }
        payload[missing_field] = ""

        response = requests.post(Urls.LOGIN_COURIER, json=payload)

        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json().get("message", "")

    @allure.title("Ошибка при авторизации с неверным логином или паролем")
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_courier_wrong_credentials_error(self, created_courier, wrong_field):
        payload = {
            "login": created_courier["login"],
            "password": created_courier["password"]
        }
        payload[wrong_field] = generate_random_string(12)

        response = requests.post(Urls.LOGIN_COURIER, json=payload)

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message", "")

    @allure.title("Ошибка при авторизации под несуществующим пользователем")
    def test_login_nonexistent_courier_error(self):
        payload = {
            "login": generate_random_string(15),
            "password": generate_random_string(15)
        }
        response = requests.post(Urls.LOGIN_COURIER, json=payload)

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message", "")