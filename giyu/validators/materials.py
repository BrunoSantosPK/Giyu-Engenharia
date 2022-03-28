import json
from flask import request
from validator import validate
from giyu.controllers.pipeline import CustomResponse


class MaterialValidator:
    
    @staticmethod
    def new_material():
        request_body = request.data if request.data != b"" else "{ }"
        body = json.loads(request_body)

        rule = {
            "description": "required|string|min:10",
            "type": "required|integer|min:1",
            "creator": "required|integer|min:1"
        }
        result, _, errors = validate(body, rule, return_info=True)

        res = CustomResponse()
        res.set_status(200 if result else 400)
        res.set_attr("message", json.dumps(errors))

        return res
