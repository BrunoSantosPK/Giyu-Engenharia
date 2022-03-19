import random
import requests


def generic_engineer():
    # Retira o "a" para evitar a possibilidade de ter "admin"
    chars = "acdefghiklmnopqrstuvxzw"
    user = ""

    while len(user) < 8:
        i = random.randint(0, len(chars) - 1)
        user = user + chars[i]

    return user


def test_get_without_valid_headers():
    heads = [
        {},
        {"id": "0"},
        {"id": "", "token": "asdsfasdf"},
        {"token": "sdfasdfasfd"},
        {"id": "0", "token": ""}
    ]
    codes = []

    for head in heads:
        res = requests.get("http://localhost:3636/engineer", headers=head)
        data = res.json()
        codes.append(data["statusCode"])

    assert 200 not in codes


def test_get_all_without_valid_jwt():
    body = {"user": "admin"}
    login = requests.post("http://localhost:3636/login", json=body).json()

    head = {"token": "asdfasdfsadf", "id": str(login["idUser"])}
    res = requests.get("http://localhost:3636/engineer", headers=head)
    data = res.json()

    assert data["statusCode"] == 401


def test_get_all_engineers():
    body = {"user": "admin"}
    login = requests.post("http://localhost:3636/login", json=body).json()

    head = {"token": login["token"], "id": str(login["idUser"])}
    res = requests.get("http://localhost:3636/engineer", headers=head)
    data = res.json()

    assert data["statusCode"] == 200 and "data" in data.keys() and len(data["data"]) > 0


def test_get_all_engineers_long_page():
    body = {"user": "admin"}
    login = requests.post("http://localhost:3636/login", json=body).json()

    head = {"token": login["token"], "id": str(login["idUser"])}
    res = requests.get("http://localhost:3636/engineer?page=100", headers=head)
    data = res.json()

    assert data["statusCode"] == 200 and "data" in data.keys() and len(data["data"]) == 0


def test_new_engineer_without_auth():
    req = {"name": generic_engineer(), "title": "Engenheiro", "creator": 1}
    res = requests.post("http://localhost:3636/engineer", json=req)
    data = res.json()
    assert data["statusCode"] == 401


def test_new_engineer_wrong_body():
    body = {"user": "admin"}
    login = requests.post("http://localhost:3636/login", json=body).json()
    head = {"token": login["token"], "id": str(login["idUser"])}

    reqs = [
        {},
        {"name": ""}, {"title": ""}, {"creator": 0},
        {"name": "", "title": ""}, {"name": "", "creator": 0}, {"title": "", "creator": 0},
        {"name": "teste", "title": "engenheiro", "creator": 0},
        {"name": "teste", "title": "eng", "creator": 1},
        {"name": "teste", "title": "engenheiro", "creator": 1},
        {"name": "teste teste", "title": "eng", "creator": 1},
        {"name": "teste teste", "title": "engenheiro", "creator": 0}
    ]
    codes = []

    for req in reqs:
        res = requests.post("http://localhost:3636/engineer", json=req, headers=head)
        data = res.json()
        codes.append(data["statusCode"])

    assert 200 not in codes


def test_new_engineer_exist_name():
    body = {"user": "admin"}
    login = requests.post("http://localhost:3636/login", json=body).json()
    head = {"token": login["token"], "id": str(login["idUser"])}

    req = {"name": "Bruno Santos", "title": "Engenheiro", "creator": 1}
    res = requests.post("http://localhost:3636/engineer", json=req, headers=head)

    data = res.json()
    assert data["statusCode"] == 444


def test_new_engineer_success():
    body = {"user": "admin"}
    login = requests.post("http://localhost:3636/login", json=body).json()
    head = {"token": login["token"], "id": str(login["idUser"])}

    req = {"name": generic_engineer(), "title": "Engenheiro Teste", "creator": 1}
    res = requests.post("http://localhost:3636/engineer", json=req, headers=head)

    data = res.json()
    assert data["statusCode"] == 200
