from flask import Flask
from dotenv import load_dotenv
from giyu.controllers.pipeline import Pipeline
from giyu.validators.users import UserValidator
from giyu.controllers.users import UserController
from giyu.validators.engineers import EngineerValidator
from giyu.controllers.engineers import EngineerController


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


@application.route("/engineer", methods=["GET"])
def get_engineers():
    return Pipeline.run(
        EngineerValidator.get_all,
        EngineerController.get_all
    )
