class Urls:
    BASE_URL = "https://qa-scooter" + ".praktikum-services.ru"
    CREATE_COURIER = f"{BASE_URL}/api/v1/courier"
    LOGIN_COURIER = f"{BASE_URL}/api/v1/courier/login"
    DELETE_COURIER = f"{BASE_URL}/api/v1/courier/"
    ORDERS = f"{BASE_URL}/api/v1/orders"
    CANCEL_ORDER = f"{BASE_URL}/api/v1/orders/cancel"


class OrderData:
    BASE_ORDER = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "ул. Пушкина, д. 10",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2026-12-01",
        "comment": "Позвонить за час"
    }