import json
from flask import request
from validator import validate
from giyu.controllers.pipeline import CustomResponse


class ItemValidator:

    @staticmethod
    def new_item() -> CustomResponse:
        request_body = request.data if request.data != b"" else "{ }"
        body = json.loads(request_body)

        rule = {
            "material": "required|integer|min:1",
            "seller": "required|integer|min:1",
            "creator": "required|integer|min:1",
            "unitPrice": "required|integer|min:1",
            "minDiscount": "required|integer|min:1",
            "discountPrice": "required|integer|min:1"
        }
        result, _, errors = validate(body, rule, return_info=True)

        res = CustomResponse()
        res.set_status(200 if result else 400)
        res.set_attr("message", json.dumps(errors))
        print(body, rule, res.get_json())

        return res

    @staticmethod
    def update_item() -> CustomResponse:
        request_body = request.data if request.data != b"" else "{ }"
        body = json.loads(request_body)

        rule = {
            "item": "required|integer|min:1",
            "editor": "required|integer|min:1",
            "unitPrice": "required|float|min:0",
            "minDiscount": "required|integer|min:1",
            "discountPrice": "required|float|min:0",
            "active": "required|boolean"
        }
        result, _, errors = validate(body, rule, return_info=True)

        res = CustomResponse()
        res.set_status(200 if result else 400)
        res.set_attr("message", json.dumps(errors))

        return res
