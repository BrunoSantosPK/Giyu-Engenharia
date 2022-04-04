import sys
from dotenv import load_dotenv
from giyu.models.entities import create_tables, drop_tables
from giyu.models.seed import seed_users, seed_engineers, seed_sellers,\
    seed_materials, seed_items


load_dotenv("config/app.env")


def init_db():
    create_tables()


def drop_db():
    drop_tables()


def seed():
    seed_users()
    seed_engineers()
    seed_sellers()
    seed_materials()
    seed_items()


def reset():
    drop_tables()
    create_tables()
    seed()


if __name__ == "__main__":
    args = sys.argv
    globals()[args[1]]()
