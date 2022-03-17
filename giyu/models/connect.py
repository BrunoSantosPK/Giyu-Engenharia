import os
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
from sqlalchemy import create_engine


def get_engine() -> Engine:
    user = os.getenv("USERPG")
    pw = os.getenv("PASSWORD")
    db = os.getenv("DATABASE")
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    return create_engine(f"postgresql://{user}:{pw}@{host}:{port}/{db}")


def get_session() -> Session:
    engine = get_engine()
    return Session(engine)
