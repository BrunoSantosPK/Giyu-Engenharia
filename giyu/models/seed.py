from datetime import datetime
from giyu.models.connect import get_session
from giyu.models.entities import Users, Engineers, Sellers,\
    MaterialsTypes, Materials, Items


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


def seed_items():
    session = get_session()
    dt = datetime.utcnow()
    data = [
        Items(CreateUserId=1, MaterialId=1, SellerId=1, UnitPrice=1200.56, MinForDiscount=10, UnitPriceWithDiscount=1103.56, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=1, SellerId=2, UnitPrice=1500.99, MinForDiscount=15, UnitPriceWithDiscount=900.84, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=3, SellerId=1, UnitPrice=15.62, MinForDiscount=11, UnitPriceWithDiscount=13.69, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=3, SellerId=2, UnitPrice=16.62, MinForDiscount=10, UnitPriceWithDiscount=12.62, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=3, SellerId=3, UnitPrice=12.95, MinForDiscount=10, UnitPriceWithDiscount=11.99, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=5, SellerId=2, UnitPrice=22.62, MinForDiscount=12, UnitPriceWithDiscount=21.74, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=5, SellerId=3, UnitPrice=25.95, MinForDiscount=13, UnitPriceWithDiscount=23.65, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=7, SellerId=1, UnitPrice=0.30, MinForDiscount=200, UnitPriceWithDiscount=0.29, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=7, SellerId=2, UnitPrice=0.32, MinForDiscount=300, UnitPriceWithDiscount=0.28, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=8, SellerId=1, UnitPrice=45.69, MinForDiscount=10, UnitPriceWithDiscount=44.32, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=8, SellerId=2, UnitPrice=49.98, MinForDiscount=12, UnitPriceWithDiscount=43.95, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=8, SellerId=3, UnitPrice=51.95, MinForDiscount=16, UnitPriceWithDiscount=41.16, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=9, SellerId=1, UnitPrice=65.11, MinForDiscount=21, UnitPriceWithDiscount=64.95, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=9, SellerId=3, UnitPrice=66.65, MinForDiscount=22, UnitPriceWithDiscount=64.94, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=11, SellerId=2, UnitPrice=36.52, MinForDiscount=20, UnitPriceWithDiscount=31.46, CreateOn=dt),
        Items(CreateUserId=1, MaterialId=11, SellerId=3, UnitPrice=32.46, MinForDiscount=20, UnitPriceWithDiscount=31.87, CreateOn=dt)
    ]

    try:
        session.add_all(data)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
