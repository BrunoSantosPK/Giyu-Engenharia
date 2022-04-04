import json
from flask import request
from validator import validate
from giyu.controllers.pipeline import CustomResponse


class ItemValidator:

    @staticmethod
    def new_item() -> CustomResponse:
        pass

    @staticmethod
    def update_item() -> CustomResponse:
        pass
