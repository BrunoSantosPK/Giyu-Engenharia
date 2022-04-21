import requests


def get_base_url():
    return "http://localhost:3636"


def success_login():
    body = {"user": "admin"}
    login = requests.post(f"{get_base_url()}/login", json=body).json()
    return login["token"], str(login["idUser"])


def test_wrong_header(route: str, method="get", body={}):
    heads = [
        {},
        {"id": "0"},
        {"id": "", "token": "asdsfasdf"},
        {"token": "sdfasdfasfd"},
        {"id": "0", "token": ""}
    ]
    codes = []

    for head in heads:
        if method == "get":
            res = requests.get(f"{get_base_url()}/{route}", headers=head)
        elif method == "post":
            res = requests.post(f"{get_base_url()}/{route}", headers=head, json=body)
        elif method == "put":
            res = requests.put(f"{get_base_url()}/{route}", headers=head, json=body)

        data = res.json()
        codes.append(data["statusCode"])

    return codes


def test_wrong_jwt(route: str, method="get", body={}):
    head = {"token": "asdfasdfsadf", "id": "1"}
    if method == "get":
        res = requests.get(f"{get_base_url()}/{route}", headers=head)
    elif method == "post":
        res = requests.post(f"{get_base_url()}/{route}", headers=head, json=body)
    elif method == "put":
        res = requests.put(f"{get_base_url()}/{route}", headers=head, json=body)

    data = res.json()
    return data["statusCode"]
