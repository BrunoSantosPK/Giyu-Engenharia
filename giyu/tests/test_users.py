import random
import requests


def generic_user():
    # Retira o "a" para evitar a possibilidade de ter "admin"
    chars = "bcdefghijklmnopqrstuvxzw"
    user = ""

    while len(user) < 5:
        i = random.randint(0, len(chars) - 1)
        user = user + chars[i]

    return user


def test_wrong_req_new_user():
    reqs = [{}, {"user": 0}, {"user": "abdc"}]
    codes = []

    for req in reqs:
        res = requests.post("http://localhost:3636/user", json=req)
        data = res.json()
        codes.append(data["statusCode"])

    assert 200 not in codes


def test_existing_user():
    req = {"user": "admin"}
    res = requests.post("http://localhost:3636/user", json=req)
    
    data = res.json()
    assert data["statusCode"] == 444


def test_add_user():
    req = {"user": generic_user()}
    res = requests.post("http://localhost:3636/user", json=req)

    data = res.json()
    assert data["statusCode"] == 200


def test_wrong_req_login():
    reqs = [{}, {"user": 0}, {"user": "abdc"}]
    codes = []

    for req in reqs:
        res = requests.post("http://localhost:3636/login", json=req)
        data = res.json()
        codes.append(data["statusCode"])

    assert 200 not in codes


def test_user_not_valid():
    req = {"user": "asfggq"}
    res = requests.post("http://localhost:3636/login", json=req)

    data = res.json()
    assert data["statusCode"] == 401


def test_real_login():
    req = {"user": "admin"}
    res = requests.post("http://localhost:3636/login", json=req)

    data = res.json()
    assert data["statusCode"] == 200
