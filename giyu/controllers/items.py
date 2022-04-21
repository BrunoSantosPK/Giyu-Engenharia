import math
import json
from flask import request
from datetime import datetime
from giyu.models.connect import get_session
from giyu.controllers.pipeline import CustomResponse, Token
from giyu.models.entities import Users, Items, Materials, Sellers


class ItemController:

    @staticmethod
    def get_items_by_seller() -> CustomResponse:
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
                # Recupera query param (paginação) e id do vendedor
                page = request.args.get("page", default=1, type=int)
                seller_id = request.view_args["id"]
                per_page = 10

                # Recupera vendedores para o item informado
                q = session.query(
                    Items.Id,
                    Items.Active,
                    Materials.Description,
                    Sellers.Name,
                    Items.UnitPrice,
                    Items.MinForDiscount,
                    Items.UnitPriceWithDiscount
                ).filter(
                    Items.SellerId == seller_id,
                    Items.MaterialId == Materials.Id,
                    Items.SellerId == Sellers.Id
                )

                total_data = q.slice((page * per_page) - per_page, page * per_page).all()
                total_pages = math.ceil(q.count() / per_page)

                # Cria a resposta enviada para o cliente
                data = [{
                    "idItem": o.Id,
                    "active": o.Active,
                    "materialDescription": o.Description,
                    "sellerName": o.Name,
                    "unitPrice": o.UnitPrice,
                    "minForDiscount": o.MinForDiscount,
                    "unitPriceWithDiscount": o.UnitPriceWithDiscount
                } for o in total_data]

                route_response.set_attr("data", data)
                route_response.set_attr("page", page)
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
    def get_sellers_by_item() -> CustomResponse:
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
                # Recupera query param (paginação) e id do material
                page = request.args.get("page", default=1, type=int)
                material_id = request.view_args["id"]
                per_page = 10

                # Recupera vendedores para o item informado
                q = session.query(
                    Items.Id,
                    Items.Active,
                    Materials.Description,
                    Sellers.Name,
                    Items.UnitPrice,
                    Items.MinForDiscount,
                    Items.UnitPriceWithDiscount
                ).filter(
                    Items.MaterialId == material_id,
                    Items.MaterialId == Materials.Id,
                    Items.SellerId == Sellers.Id
                )

                total_data = q.slice((page * per_page) - per_page, page * per_page).all()
                total_pages = math.ceil(q.count() / per_page)

                # Cria a resposta enviada para o cliente
                data = [{
                    "idItem": o.Id,
                    "active": o.Active,
                    "materialDescription": o.Description,
                    "sellerName": o.Name,
                    "unitPrice": o.UnitPrice,
                    "minForDiscount": o.MinForDiscount,
                    "unitPriceWithDiscount": o.UnitPriceWithDiscount
                } for o in total_data]

                route_response.set_attr("data", data)
                route_response.set_attr("page", page)
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
    def new_item() -> CustomResponse:
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

            # Regras de negócio:
            # 0. Transformar preços de inteiro pra decimal
            # 1. Verificar se o preço unitário é maior que 0
            # 2. Verificar se o preço com desconto é menor que o unitário
            # 3. Verificar se o material + vendedor já está cadastrado

        except BaseException as e:
            # Captura erros internos
            session.rollback()
            route_response.set_status(500)
            route_response.set_message(str(e))

        finally:
            session.close()

        return route_response

    @staticmethod
    def update_item() -> CustomResponse:
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

        except BaseException as e:
            # Captura erros internos
            session.rollback()
            route_response.set_status(500)
            route_response.set_message(str(e))
            
        finally:
            session.close()

        return route_response
