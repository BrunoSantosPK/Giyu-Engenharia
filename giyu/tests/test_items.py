import generic
import requests


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
    pass


def test_new_item_invalid_body():
    pass


def test_new_item_without_jwt():
    req = {
        "material": 1,
        "seller": 1,
        "creator": 1,
        "unitPrice": 150,
        "minDiscount": 2,
        "discountPrice": 130
    }
    
    res_invalid = generic.test_wrong_header("item", method="post", body=req)
    res_not_auth = generic.test_wrong_jwt("item", method="post", body=req)
    assert 200 not in res_invalid and res_not_auth == 401


def test_new_item_already_registered():
    pass


def test_new_item_wrong_discount():
    pass


def test_update_item():
    pass


def test_update_item_without_jwt():
    pass


def test_update_item_wrong_body():
    pass


def test_update_item_wrong_discount():
    pass
