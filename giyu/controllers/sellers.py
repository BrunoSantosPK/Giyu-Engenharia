import math
import json
from flask import request
from datetime import datetime
from giyu.models.connect import get_session
from giyu.models.entities import Sellers, Users
from giyu.controllers.pipeline import CustomResponse, Token


class SellerController:
    
    @staticmethod
    def get_all() -> CustomResponse:
        # Recupera dados de requisição e inicia variáveis de controle
        route_response = CustomResponse()
        header = request.headers
        session = get_session()
        valid = True

        try:
            # Valida token jwt
            token = header["token"]
            id_user = int(header["id"])
            success, msg = Token.validate(token, id_user)

            if not success:
                valid = False
                route_response.set_status(401)
                route_response.set_message(msg)

            if valid:
                # Recupera query param (paginação)
                page = request.args.get("page", default=1, type=int)
                per_page = 10

                # Recupera dados de engenheiros cadastrados
                q = session.query(
                    Sellers.Id,
                    Users.UserName,
                    Sellers.Name,
                    Sellers.CreateOn
                ).filter(
                    Sellers.UserId == Users.Id
                )

                total_data = q.slice((page * per_page) - per_page, page * per_page).all()
                total_pages = math.ceil(q.count() / per_page)

                # Cria a resposta enviada para o cliente
                data = [{
                    "idSeller": o.Id,
                    "createdBy": o.UserName,
                    "createdOn": o.CreateOn.isoformat(),
                    "sellerName": o.Name
                } for o in total_data]
                route_response.set_attr("data", data)
                route_response.set_attr("totalPages", total_pages)

        except BaseException as e:
            # Captura erros internos
            session.rollback()
            route_response.set_status(500)
            route_response.set_message(str(e))

        finally:
            session.close()

        return route_response

    @staticmethod
    def new_seller() -> CustomResponse:
        # Recupera dados de requisição e inicia variáveis de controle
        route_response = CustomResponse()
        body = json.loads(request.data)
        header = request.headers
        session = get_session()
        valid = True

        try:
            # Valida token jwt
            token = header["token"]
            id_user = int(header["id"])
            success, msg = Token.validate(token, id_user)

            if not success:
                valid = False
                route_response.set_status(401)
                route_response.set_message(msg)

            # Verifica se o nome já existe na base de dados
            if valid:
                q = session.query(Sellers).filter_by(Name=body["name"].upper())
                if len(q.all()) != 0:
                    valid = False
                    route_response.set_status(444)
                    route_response.set_message("Engenheiro já cadastrado")

            # Faz a inclusão no banco de dados
            if valid:
                session.add(Sellers(
                    UserId=body["creator"],
                    Name=body["name"].upper(),
                    CreateOn=datetime.utcnow()
                ))
                session.commit()
                
        except BaseException as e:
            # Captura erros internos
            session.rollback()
            route_response.set_status(500)
            route_response.set_message(str(e))

        finally:
            session.close()

        return route_response
