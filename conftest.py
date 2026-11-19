import pytest
import requests
from data import Urls
from helpers import generate_courier_payload


@pytest.fixture
def courier_data():
    payload = generate_courier_payload()
    yield payload

    login_response = requests.post(
        Urls.LOGIN_COURIER,
        json={"login": payload["login"], "password": payload["password"]}
    )
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        requests.delete(f"{Urls.DELETE_COURIER}{courier_id}")


@pytest.fixture
def created_courier(courier_data):
    requests.post(Urls.CREATE_COURIER, json=courier_data)
    return courier_data