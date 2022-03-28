import math
import json
from flask import request
from datetime import datetime
from giyu.models.connect import get_session
from giyu.controllers.pipeline import CustomResponse, Token
from giyu.models.entities import Materials, Users, MaterialsTypes


class MaterialController:

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

                # Recupera dados de materiais cadastrados
                q = session.query(
                    Materials.Id,
                    Users.UserName,
                    MaterialsTypes.Tag,
                    Materials.Description,
                    Materials.CreateOn
                ).filter(
                    Materials.UserId == Users.Id,
                    Materials.MaterialTypeId == MaterialsTypes.Id
                )

                total_data = q.slice((page * per_page) - per_page, page * per_page).all()
                total_pages = math.ceil(q.count() / per_page)

                # Cria a resposta enviada para o cliente
                data = [{
                    "idMaterial": o.Id,
                    "typeMaterial": o.Tag,
                    "description": o.Description,
                    "createdBy": o.UserName,
                    "createdOn": o.CreateOn.isoformat()
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
    def new_material() -> CustomResponse:
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
                q = session.query(Materials).filter_by(Description=body["description"].upper())
                if len(q.all()) != 0:
                    valid = False
                    route_response.set_status(444)
                    route_response.set_message("Material já cadastrado")


            # Faz a inclusão no banco de dados
            if valid:
                session.add(Materials(
                    UserId=body["creator"],
                    MaterialTypeId=body["type"],
                    Description=body["description"].upper(),
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

    @staticmethod
    def get_material_types() -> CustomResponse:
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
                # Recupera tipos de materiais possíveis
                q = session.query(MaterialsTypes)
                data = [{"idType": o.Id, "typeMaterial": o.Tag} for o in q.all()]
                route_response.set_attr("data", data)

        except BaseException as e:
            # Captura erros internos
            session.rollback()
            route_response.set_status(500)
            route_response.set_message(str(e))

        finally:
            session.close()

        return route_response
