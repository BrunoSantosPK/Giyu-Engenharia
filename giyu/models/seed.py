from datetime import datetime
from giyu.models.connect import get_session
from giyu.models.entities import Users, Engineers, Sellers,\
    MaterialsTypes, Materials


def seed_users():
    session = get_session()
    data = [
        Users(UserName="admin", CreateOn=datetime.utcnow())
    ]

    try:
        session.add_all(data)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()


def seed_engineers():
    session = get_session()
    dt = datetime.utcnow()
    data = [
        Engineers(UserId=1, Name="BRUNO SANTOS", Title="Engenheiro Químico", CreateOn=dt),
        Engineers(UserId=1, Name="JEAN MEIRELES", Title="Engenheiro Civil", CreateOn=dt)
    ]

    try:
        session.add_all(data)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()


def seed_sellers():
    session = get_session()
    dt = datetime.utcnow()
    data = [
        Sellers(UserId=1, Name="CONSTRUÇÕES XYZ", CreateOn=dt),
        Sellers(UserId=1, Name="CONSTRUTORA ABC", CreateOn=dt),
        Sellers(UserId=1, Name="MATERIAIS S.A.", CreateOn=dt),
        Sellers(UserId=1, Name="CONSTRUMAT", CreateOn=dt)
    ]

    try:
        session.add_all(data)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()


def seed_materials():
    session = get_session()
    dt = datetime.utcnow()
    data_types = [
        MaterialsTypes(Tag="Mão de obra"),
        MaterialsTypes(Tag="Material")
    ]
    data_materials = [
        Materials(UserId=1, MaterialTypeId=1, Description="EQUIPE 4PE + 2SE", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=1, Description="EQUIPE 5PE + 3SE", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="AÇO CA 60", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="AÇO CA 50", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="ARAME RECOZIDO", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="AREIA LAVADA", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="TIJOLO MACIÇO", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="ARGAMASSA INDUSTRIAL", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="BRITA 0", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="BRITA 1", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="CIMENTO PORTLAND", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="PREGO 15X15", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="CERÂMICA DE FACHADA", CreateOn=dt),
        Materials(UserId=1, MaterialTypeId=2, Description="CERÂMICA DE PISO", CreateOn=dt)
    ]

    try:
        session.add_all(data_types)
        session.commit()
        session.add_all(data_materials)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
