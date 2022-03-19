import json
from flask import request
from validator import validate
from giyu.controllers.pipeline import CustomResponse


class GenericValidator:

    @staticmethod
    def auth_header():
        body = request.headers
        rule = {"token": "required|string|min:1", "id": "required|string|min:1"}
        result, _, errors = validate(body, rule, return_info=True)

        res = CustomResponse()
        res.set_status(200 if result else 401)
        res.set_attr("message", json.dumps(errors))

        return res
