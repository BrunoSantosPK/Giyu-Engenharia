import os
import jwt
import json
from typing import Callable, Tuple
from datetime import datetime, timedelta


class CustomResponse:

    def __init__(self):
        self.__body = {
            "statusCode": 200,
            "message": ""
        }

    def set_status(self, valor: int):
        '''
        Define o status para response. Alguns padrões:
        200: sucesso
        400: requisição inválida
        401: usuário não autorizado
        444: regra de negócio não atendida
        445: erro de código
        '''
        self.__body["statusCode"] = valor

    def set_message(self, message: str):
        self.__body["message"] = message
    
    def set_attr(self, attr: str, valor: any):
        self.__body[attr] = valor

    def get_status(self) -> int:
        return self.__body["statusCode"]

    def get_json(self) -> str:
        return json.dumps(self.__body)


class Pipeline():

    @staticmethod
    def run(*args: Callable[[], CustomResponse]) -> str:
        for func in args:
            res = func()
            if res.get_status() != 200:
                break

        return res.get_json()


class Token:
    
    @staticmethod
    def create(id: int) -> Tuple[bool, str]:
        secret = os.getenv("SECRET")
        payload = {
            "exp": datetime.utcnow() + timedelta(days=1),
            "iat": datetime.utcnow(),
            "sub": id
        }

        try:
            token = str(jwt.encode(payload, secret, algorithm="HS256"))
            success = True
        except Exception as e:
            success = False
            token = str(e)
    
        return success, token
    

    @staticmethod
    def validate(token: str, id: int) -> Tuple[bool, str]:
        secret = os.getenv("SECRET")
        success, msg = True, ""

        try:
            payload = jwt.decode(token, secret, algorithms="HS256")
            if payload["sub"] != id:
                success = False
                msg = "Token não relacionado ao usuário."

        except jwt.ExpiredSignatureError:
            success = False
            msg = "Validade do token expirada."

        except jwt.InvalidTokenError:
            success = False
            msg = "Formato do token inválido."

        except BaseException as e:
            success = False
            msg = str(e)

        finally:
            return success, msg
