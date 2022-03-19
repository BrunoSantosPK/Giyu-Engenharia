from datetime import datetime
from giyu.models.connect import get_session
from giyu.models.entities import Users, Engineers


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
