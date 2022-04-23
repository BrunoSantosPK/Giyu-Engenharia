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

            # Regra de negócio: o preço com desconto deve ser menor que o preço unitário
            if valid:
                if body["discountPrice"] >= body["unitPrice"]:
                    valid = False
                    route_response.set_status(444)
                    route_response.set_message("Preço com desconto maior ou igual ao preço unitário.")

            # Regra de negócio: os preços devem ser maiores que zero
            if valid:
                if body["discountPrice"] <= 0 or body["unitPrice"] <= 0:
                    valid = False
                    route_response.set_status(444)
                    route_response.set_message("Os preços devem ser maiores que 0.")

            # Regra de negócio: a quantidade para conceder desconto deve ser maior que 1
            if valid:
                if body["minDiscount"] <= 1:
                    valid = False
                    route_response.set_status(444)
                    route_response.set_message("A quantidade para desconto deve ser maior que 1.")

            # Verifica se material e vendedor já estão cadastrados
            if valid:
                q = session.query(Items).filter_by(
                    MaterialId=body["material"],
                    SellerId=body["seller"]
                )
                if len(q.all()) != 0:
                    valid = False
                    route_response.set_status(444)
                    route_response.set_message("O material já está cadastrado para o vendedor.")

            # Procede para criação do registro no banco
            if valid:
                price = body["unitPrice"] / 100.0
                discout = body["discountPrice"] / 100.0

                session.add(Items(
                    MaterialId=body["material"],
                    SellerId=body["seller"],
                    CreateUserId=body["creator"],
                    Active=True,
                    UnitPrice=price,
                    MinForDiscount=body["minDiscount"],
                    UnitPriceWithDiscount=discout,
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

            # Regra de negócio: o preço com desconto deve ser menor que o preço unitário
            if valid:
                if body["discountPrice"] >= body["unitPrice"]:
                    valid = False
                    route_response.set_status(444)
                    route_response.set_message("Preço com desconto maior ou igual ao preço unitário.")

            # Regra de negócio: os preços devem ser maiores que zero
            if valid:
                if body["discountPrice"] <= 0 or body["unitPrice"] <= 0:
                    valid = False
                    route_response.set_status(444)
                    route_response.set_message("Os preços devem ser maiores que 0.")

            # Regra de negócio: a quantidade para conceder desconto deve ser maior que 1
            if valid:
                if body["minDiscount"] <= 1:
                    valid = False
                    route_response.set_status(444)
                    route_response.set_message("A quantidade para desconto deve ser maior que 1.")

            # Procede para criação do registro no banco
            if valid:
                session.query(Items).filter_by(Id=body["item"]).update({
                    "EditUserId": body["editor"],
                    "UnitPrice": body["unitPrice"] / 100.0,
                    "MinForDiscount": body["minDiscount"],
                    "UnitPriceWithDiscount": body["discountPrice"] / 100.0,
                    "Active": body["active"],
                    "EditOn": datetime.utcnow()
                })
                session.commit()

        except BaseException as e:
            # Captura erros internos
            session.rollback()
            route_response.set_status(500)
            route_response.set_message(str(e))
            
        finally:
            session.close()

        return route_response
