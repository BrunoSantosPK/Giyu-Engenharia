import json
from flask import request
from datetime import datetime
from giyu.models.entities import Users
from giyu.models.connect import get_session
from giyu.controllers.pipeline import CustomResponse, Token


class UserController:

    @staticmethod
    def new_user() -> CustomResponse:
        # Recupera dados de requisição e inicia variáveis de controle
        route_response = CustomResponse()
        body = json.loads(request.data)
        session = get_session()
        valid = True

        try:
            # Verifica se o usuário já está cadastrado
            q = session.query(Users).filter_by(UserName=body["user"])
            if len(q.all()) != 0:
                valid = False
                route_response.set_status(444)
                route_response.set_message("Usuário já cadastrado")

            # Faz a inserção
            if valid:
                dt = datetime.utcnow()
                session.add(Users(UserName=body["user"], CreateOn=dt))
                session.commit()

        except BaseException as e:
            # Captura erros internos
            session.rollback()
            route_response.set_status(500)
            route_response.set_message(str(e))
            
        finally:
            session.close()
        
        return route_response

    @staticmethod
    def login() -> CustomResponse:
        # Recupera dados de requisição e inicia variáveis de controle
        route_response = CustomResponse()
        body = json.loads(request.data)
        session = get_session()

        try:
            # Verifica se o usuário está cadastrado
            q = session.query(Users).filter_by(UserName=body["user"])
            if len(q.all()) == 0:
                route_response.set_status(401)
                route_response.set_message("Usuário não cadastrado")

            else:
                # Cria o token jwt
                reg = q.first()
                success, token = Token.create(reg.Id)

                if success:
                    route_response.set_attr("token", token)
                    route_response.set_attr("idUser", reg.Id)
                else:
                    route_response.set_status(500)
                    route_response.set_message(token)

        except BaseException as e:
            # Captura erros internos
            session.rollback()
            route_response.set_status(500)
            route_response.set_message(str(e))

        finally:
            session.close()

        return route_response
