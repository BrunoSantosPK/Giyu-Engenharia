import requests


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
