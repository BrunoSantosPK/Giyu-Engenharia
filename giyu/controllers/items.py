import math
import json
from flask import request
from datetime import datetime
from giyu.models.connect import get_session
from giyu.controllers.pipeline import CustomResponse, Token
from giyu.models.entities import Users, Items


class ItemController:

    @staticmethod
    def get_items_by_seller() -> CustomResponse:
        pass

    @staticmethod
    def get_sellers_by_item() -> CustomResponse:
        pass

    @staticmethod
    def new_item() -> CustomResponse:
        pass

    @staticmethod
    def update_item() -> CustomResponse:
        pass
