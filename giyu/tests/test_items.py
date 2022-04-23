import random
import generic
import requests


def generate_add(material: int, seller: int, creator: int, price: int, quantity: int, discount: int):
    return {
        "material": material,
        "seller": seller,
        "creator": creator,
        "unitPrice": price,
        "minDiscount": quantity,
        "discountPrice": discount
    }


def generate_upd(item: int, editor: int, price: int, quantity: int, discount: int, active: int):
    return {
        "item": item,
        "editor": editor,
        "unitPrice": price,
        "minDiscount": quantity,
        "discountPrice": discount,
        "active": active
    }


def test_get_sellers_by_material_id():
    token, id_user = generic.success_login()
    head = {"token": token, "id": id_user}

    res = requests.get(f"{generic.get_base_url()}/item/3", headers=head)
    data = res.json()
    assert data["statusCode"] == 200 and "data" in data.keys() and len(data["data"]) >= 3


def test_get_sellers_by_material_id_without_jwt():
    res_invalid = generic.test_wrong_header("item/3")
    res_not_auth = generic.test_wrong_jwt("item/3")
    assert 200 not in res_invalid and res_not_auth == 401


def test_get_sellers_by_material_id_long_page():
    token, id_user = generic.success_login()
    head = {"token": token, "id": id_user}

    res = requests.get(f"{generic.get_base_url()}/item/3?page=200", headers=head)
    data = res.json()
    assert data["statusCode"] == 200 and "data" in data.keys() and len(data["data"]) == 0


def test_get_items_by_seller():
    token, id_user = generic.success_login()
    head = {"token": token, "id": id_user}

    res = requests.get(f"{generic.get_base_url()}/item/seller/1", headers=head)
    data = res.json()
    assert data["statusCode"] == 200 and "data" in data.keys() and len(data["data"]) >= 5


def test_get_items_by_seller_without_jwt():
    res_invalid = generic.test_wrong_header("item/seller/1")
    res_not_auth = generic.test_wrong_jwt("item/seller/1")
    assert 200 not in res_invalid and res_not_auth == 401


def test_get_items_by_seller_long_page():
    token, id_user = generic.success_login()
    head = {"token": token, "id": id_user}

    res = requests.get(f"{generic.get_base_url()}/item/seller/1?page=200", headers=head)
    data = res.json()
    assert data["statusCode"] == 200 and "data" in data.keys() and len(data["data"]) == 0


def test_new_item():
    token, id_user = generic.success_login()
    head = {"token": token, "id": id_user}
    cont, limit, success = 0, 200, False

    while True:
        if cont > limit:
            success = True
            break

        material = random.randint(1, 14)
        seller = random.randint(1, 4)
        price = random.randint(100, 10000)
        discount = int(random.random() * price)

        req = generate_add(material, seller, 1, price, random.randint(3, 10), discount)
        res = requests.post(f"{generic.get_base_url()}/item", json=req, headers=head)
        status = res.json()["statusCode"]

        if status == 200:
            success = True
            break
        else:
            cont = cont + 1

    assert success == True and cont <= limit


def test_new_item_invalid_rule():
    token, id_user = generic.success_login()
    head = {"token": token, "id": id_user}
    reqs = [
        generate_add(1, 1, 1, 100, 2, 90),
        generate_add(1, 3, 1, 100, 2, 120),
        generate_add(1, 3, 1, 100, 1, 90)
    ]

    results = []
    for req in reqs:
        res = requests.post(f"{generic.get_base_url()}/item", json=req, headers=head)
        results.append(res.json()["statusCode"])

    assert all(r == 444 for r in results)


def test_new_item_without_jwt():
    req = generate_add(1, 1, 1, 150, 2, 130)
    res_invalid = generic.test_wrong_header("item", method="post", body=req)
    res_not_auth = generic.test_wrong_jwt("item", method="post", body=req)
    assert 200 not in res_invalid and res_not_auth == 401


def test_update_item():
    token, id_user = generic.success_login()
    head = {"token": token, "id": id_user}
    
    price = random.randint(100, 10000)
    quantity = random.randint(2, 20)
    discount = int(random.random() * price)
    active = random.randint(0, 1)
    req = generate_upd(1, 1, price, quantity, discount, active)

    res = requests.put(f"{generic.get_base_url()}/item", json=req, headers=head)
    assert res.json()["statusCode"] == 200


def test_update_item_without_jwt():
    price = random.randint(100, 10000)
    quantity = random.randint(2, 20)
    discount = int(random.random() * price)
    active = random.randint(0, 1)
    req = generate_upd(1, 1, price, quantity, discount, active)

    res_invalid = generic.test_wrong_header("item", method="put", body=req)
    res_not_auth = generic.test_wrong_jwt("item", method="put", body=req)
    assert 200 not in res_invalid and res_not_auth == 401


def test_update_item_wrong_body():
    token, id_user = generic.success_login()
    head = {"token": token, "id": id_user}
    reqs = [
        generate_upd(1, 1, 150, 5, 160, 1),
        generate_upd(1, 1, 150, 1, 140, 0)
    ]

    results = []
    for req in reqs:
        res = requests.put(f"{generic.get_base_url()}/item", json=req, headers=head)
        results.append(res.json()["statusCode"])

    assert all(r == 444 for r in results)
