import random
import requests


BASE_URL = "http://localhost:3636"


def generic_material():
    chars = "abcdefghiklmnopqrstuvxzw"
    user = ""

    while len(user) < 10:
        i = random.randint(0, len(chars) - 1)
        user = user + chars[i]

    return user


def test_get_materials_without_valid_header():
    heads = [
        {},
        {"id": "0"},
        {"id": "", "token": "asdsfasdf"},
        {"token": "sdfasdfasfd"},
        {"id": "0", "token": ""}
    ]
    codes = []

    for head in heads:
        res = requests.get(f"{BASE_URL}/material", headers=head)
        data = res.json()
        codes.append(data["statusCode"])

    assert 200 not in codes


def test_get_materials_without_jwt():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()

    head = {"token": "asdfasdfsadf", "id": str(login["idUser"])}
    res = requests.get(f"{BASE_URL}/material", headers=head)
    data = res.json()

    assert data["statusCode"] == 401


def test_get_all_materials_success():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()

    head = {"token": login["token"], "id": str(login["idUser"])}
    res = requests.get(f"{BASE_URL}/material", headers=head)
    data = res.json()

    assert data["statusCode"] == 200 and "data" in data.keys() and len(data["data"]) > 0


def test_get_all_materials_long_page():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()

    head = {"token": login["token"], "id": str(login["idUser"])}
    res = requests.get(f"{BASE_URL}/material?page=100", headers=head)
    data = res.json()

    assert data["statusCode"] == 200 and "data" in data.keys() and len(data["data"]) == 0


def test_new_material_without_auth():
    req = {"name": generic_material(), "creator": 1}
    res = requests.post(f"{BASE_URL}/material", json=req)
    data = res.json()
    assert data["statusCode"] == 401


def teste_new_material_wrong_jwt():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()

    head = {"token": "asdfasdfsadf", "id": str(login["idUser"])}
    req = {"description": "teste teste", "creator": 1, "type": 2}

    res = requests.post(f"{BASE_URL}/material", json=req, headers=head)
    data = res.json()

    assert data["statusCode"] == 401


def test_new_material_wrong_body():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()
    head = {"token": login["token"], "id": str(login["idUser"])}

    reqs = [
        {},
        {"description": ""}, {"creator": 0}, {"type": 0},
        {"description": "", "creator": 1, "type": 0},
        {"description": "", "creator": 0, "type": 1},
        {"description": "", "creator": 1, "type": 2},
        {"description": "teste teste", "creator": 0, "type": 0},
        {"description": "teste teste", "creator": 0, "type": 2}
    ]
    codes = []

    for req in reqs:
        res = requests.post(f"{BASE_URL}/material", json=req, headers=head)
        data = res.json()
        codes.append(data["statusCode"])

    assert 200 not in codes


def test_new_material_exist_name():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()
    head = {"token": login["token"], "id": str(login["idUser"])}

    req = {"description": "AREIA LAVADA", "creator": 1, "type": 2}
    res = requests.post(f"{BASE_URL}/material", json=req, headers=head)

    data = res.json()
    assert data["statusCode"] == 444


def test_new_material_success():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()
    head = {"token": login["token"], "id": str(login["idUser"])}

    req = {"description": generic_material(), "creator": 1, "type": 2}
    res = requests.post(f"{BASE_URL}/material", json=req, headers=head)

    data = res.json()
    assert data["statusCode"] == 200


def test_get_type_materials_without_valid_header():
    heads = [
        {},
        {"id": "0"},
        {"id": "", "token": "asdsfasdf"},
        {"token": "sdfasdfasfd"},
        {"id": "0", "token": ""}
    ]
    codes = []

    for head in heads:
        res = requests.get(f"{BASE_URL}/material/types", headers=head)
        data = res.json()
        codes.append(data["statusCode"])

    assert 200 not in codes


def test_get_type_materials_without_jwt():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()

    head = {"token": "asdfasdfsadf", "id": str(login["idUser"])}
    res = requests.get(f"{BASE_URL}/material/types", headers=head)
    data = res.json()

    assert data["statusCode"] == 401


def test_get_type_materials_success():
    body = {"user": "admin"}
    login = requests.post(f"{BASE_URL}/login", json=body).json()

    head = {"token": login["token"], "id": str(login["idUser"])}
    res = requests.get(f"{BASE_URL}/material/types", headers=head)
    data = res.json()

    assert data["statusCode"] == 200 and "data" in data.keys() and len(data["data"]) == 2
