import sys
from dotenv import load_dotenv
from giyu.models.seed import seed_users, seed_engineers
from giyu.models.entities import create_tables, drop_tables


load_dotenv("config/app.env")


def init_db():
    create_tables()


def drop_db():
    drop_tables()


def seed():
    seed_users()
    seed_engineers()


def reset():
    drop_tables()
    create_tables()
    seed()


if __name__ == "__main__":
    args = sys.argv
    globals()[args[1]]()
