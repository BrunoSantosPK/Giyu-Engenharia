import random
import requests


BASE_URL = "http://localhost:3636"


def generic_seller():
    chars = "abcdefghiklmnopqrstuvxzw"
    user = ""

    while len(user) < 8:
        i = random.randint(0, len(chars) - 1)
        user = user + chars[i]

    return user


def test_get_without_valid_header():
    heads = [
        {},
        {"id": "0"},
        {"id": "", "token": "asdsfasdf"},
        {"token": "sdfasdfasfd"},
        {"id": "0", "token": ""}
    ]
    codes = []

    for head in heads:
        res = requests.get(f"{BASE_URL}/seller", headers=head)
        data = res.json()
        codes.append(data["statusCode"])

    assert 200 not in codes


def test_get_sellers_without_jwt():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()

    head = {"token": "asdfasdfsadf", "id": str(login["idUser"])}
    res = requests.get(f"{BASE_URL}/seller", headers=head)
    data = res.json()

    assert data["statusCode"] == 401


def test_get_all_sellers_success():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()

    head = {"token": login["token"], "id": str(login["idUser"])}
    res = requests.get(f"{BASE_URL}/seller", headers=head)
    data = res.json()

    assert data["statusCode"] == 200 and "data" in data.keys() and len(data["data"]) > 0


def test_get_all_sellers_long_page():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()

    head = {"token": login["token"], "id": str(login["idUser"])}
    res = requests.get(f"{BASE_URL}/seller?page=100", headers=head)
    data = res.json()

    assert data["statusCode"] == 200 and "data" in data.keys() and len(data["data"]) == 0


def test_new_seller_without_auth():
    req = {"name": generic_seller(), "creator": 1}
    res = requests.post(f"{BASE_URL}/seller", json=req)
    data = res.json()
    assert data["statusCode"] == 401


def teste_new_seller_wrong_jwt():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()

    head = {"token": "asdfasdfsadf", "id": str(login["idUser"])}
    req = {"name": "teste teste", "creator": 1}

    res = requests.post(f"{BASE_URL}/seller", json=req, headers=head)
    data = res.json()

    assert data["statusCode"] == 401


def test_new_seller_wrong_body():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()
    head = {"token": login["token"], "id": str(login["idUser"])}

    reqs = [
        {},
        {"name": ""}, {"creator": 0},
        {"name": "", "creator": 1},
        {"name": "teste teste", "creator": 0}
    ]
    codes = []

    for req in reqs:
        res = requests.post(f"{BASE_URL}/seller", json=req, headers=head)
        data = res.json()
        codes.append(data["statusCode"])

    assert 200 not in codes


def test_new_seller_exist_name():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()
    head = {"token": login["token"], "id": str(login["idUser"])}

    req = {"name": "construmat", "creator": 1}
    res = requests.post(f"{BASE_URL}/seller", json=req, headers=head)

    data = res.json()
    assert data["statusCode"] == 444


def test_new_engineer_success():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()
    head = {"token": login["token"], "id": str(login["idUser"])}

    req = {"name": generic_seller(), "creator": 1}
    res = requests.post(f"{BASE_URL}/seller", json=req, headers=head)

    data = res.json()
    assert data["statusCode"] == 200
