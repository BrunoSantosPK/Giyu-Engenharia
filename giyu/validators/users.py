import json
from flask import request
from validator import validate
from giyu.controllers.pipeline import CustomResponse


class UserValidator:
    
    @staticmethod
    def new_user() -> CustomResponse:
        request_body = request.data if request.data != b"" else "{ }"
        body = json.loads(request_body)

        rule = {"user": "required|string|min:5"}
        result, _, errors = validate(body, rule, return_info=True)

        res = CustomResponse()
        res.set_status(200 if result else 400)
        res.set_attr("message", json.dumps(errors))

        return res

    @staticmethod
    def login() -> CustomResponse:
        request_body = request.data if request.data != b"" else "{ }"
        body = json.loads(request_body)

        rule = {"user": "required|string|min:5"}
        result, _, errors = validate(body, rule, return_info=True)

        res = CustomResponse()
        res.set_status(200 if result else 400)
        res.set_attr("message", json.dumps(errors))

        return res
