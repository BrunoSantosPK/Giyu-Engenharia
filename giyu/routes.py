from dotenv import load_dotenv
from flask import Flask, request
from giyu.controllers.pipeline import Pipeline
from giyu.validators.generic import GenericValidator

from giyu.validators.users import UserValidator
from giyu.controllers.users import UserController

from giyu.validators.engineers import EngineerValidator
from giyu.controllers.engineers import EngineerController

from giyu.validators.sellers import SellerValidator
from giyu.controllers.sellers import SellerController

from giyu.validators.materials import MaterialValidator
from giyu.controllers.materials import MaterialController

from giyu.validators.items import ItemValidator
from giyu.controllers.items import ItemController


# Inicia aplicação e carrega variáveis de ambiente
load_dotenv("config/app.env")
application = Flask(__name__)


@application.route("/user", methods=["POST"])
def new_user():
    return Pipeline.run(
        UserValidator.new_user,
        UserController.new_user
    )


@application.route("/login", methods=["POST"])
def login():
    return Pipeline.run(
        UserValidator.login,
        UserController.login
    )


@application.route("/engineer", methods=["GET", "POST"])
def engineers():
    if request.method == "GET":
        return Pipeline.run(
            GenericValidator.auth_header,
            EngineerController.get_all
        )
    elif request.method == "POST":
        return Pipeline.run(
            GenericValidator.auth_header,
            EngineerValidator.new_engineer,
            EngineerController.new_engineer
        )


@application.route("/seller", methods=["GET", "POST"])
def sellers():
    if request.method == "GET":
        return Pipeline.run(
            GenericValidator.auth_header,
            SellerController.get_all
        )
    elif request.method == "POST":
        return Pipeline.run(
            GenericValidator.auth_header,
            SellerValidator.new_seller,
            SellerController.new_seller
        )


@application.route("/material", methods=["GET", "POST"])
def materials():
    if request.method == "GET":
        return Pipeline.run(
            GenericValidator.auth_header,
            MaterialController.get_all
        )
    elif request.method == "POST":
        return Pipeline.run(
            GenericValidator.auth_header,
            MaterialValidator.new_material,
            MaterialController.new_material
        )


@application.route("/material/types", methods=["GET"])
def material_types():
    return Pipeline.run(
        GenericValidator.auth_header,
        MaterialController.get_material_types
    )


@application.route("/item/<id>", methods=["GET"])
def sellers_item(id: int):
    return Pipeline.run(
        GenericValidator.auth_header,
        ItemController.get_sellers_by_item
    )


@application.route("/item/seller/<id>", methods=["GET"])
def items_seller(id: int):
    return Pipeline.run(
        GenericValidator.auth_header,
        ItemController.get_items_by_seller
    )


@application.route("/item", methods=["POST", "PUT"])
def item_manager():
    if request.method == "POST":
        return Pipeline.run(
            GenericValidator.auth_header,
            ItemValidator.new_item,
            ItemController.new_item
        )
    elif request.method == "PUT":
        return Pipeline.run(
            GenericValidator.auth_header,
            ItemValidator.update_item,
            ItemController.update_item
        )
