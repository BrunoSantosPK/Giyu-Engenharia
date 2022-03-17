from flask import request
from giyu.models.connect import get_session
from giyu.models.entities import Engineers, Users
from giyu.controllers.pipeline import CustomResponse, Token


class EngineerController:

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
                data_per_page = 10

                # Recupera dados de engenheiros cadastrados
                res = session.query(
                    Engineers.Id,
                    Users.UserName,
                    Engineers.Name,
                    Engineers.Title,
                    Engineers.CreateOn
                ).filter(
                    Engineers.UserId == Users.Id
                ).slice(
                    (page * data_per_page) - data_per_page, page * data_per_page
                ).all()

                # Cria a resposta enviada para o cliente
                data = [{
                    "idEngineer": o.Id,
                    "createdBy": o.UserName,
                    "createdOn": o.CreateOn.isoformat(),
                    "engineerName": o.Name,
                    "engineerTitle": o.Title
                } for o in res]
                route_response.set_attr("data", data)

        except BaseException as e:
            # Captura erros internos
            session.rollback()
            route_response.set_status(500)
            route_response.set_message(str(e))

        finally:
            session.close()

        return route_response

    @staticmethod
    def new_engineer():
        pass
