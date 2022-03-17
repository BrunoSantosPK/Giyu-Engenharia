import json
from flask import request
from validator import validate
from giyu.controllers.pipeline import CustomResponse


class EngineerValidator:

    @staticmethod
    def get_all():
        body = request.headers
        rule = {"token": "required|string|min:1", "id": "required|string|min:1"}
        result, _, errors = validate(body, rule, return_info=True)

        res = CustomResponse()
        res.set_status(200 if result else 400)
        res.set_attr("message", json.dumps(errors))

        return res

    def new_engineer():
        pass
