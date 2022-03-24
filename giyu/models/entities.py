from giyu.models.connect import get_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


Base = declarative_base()


class Users(Base):
    __tablename__ = "Users"
    __table_args__ = {"schema": "public"}

    Id = Column(Integer, primary_key=True)
    UserName = Column(String, nullable=False)
    CreateOn = Column(DateTime, nullable=False)


class Engineers(Base):
    __tablename__ = "Engineers"
    __table_args__ = {"schema": "planning"}

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey("public.Users.Id"), nullable=False)
    Name = Column(String, nullable=False)
    Title = Column(String, nullable=False)
    CreateOn = Column(DateTime, nullable=False)


class Sellers(Base):
    __tablename__ = "Sellers"
    __table_args__ = {"schema": "shop"}

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey("public.Users.Id"), nullable=False)
    Name = Column(String, nullable=False)
    CreateOn = Column(DateTime, nullable=False)


def create_tables():
    Base.metadata.create_all(get_engine())


def drop_tables():
    Base.metadata.drop_all(get_engine())


'''class MaterialsTypes(Base):
    __tablename__ = "MaterialsTypes"
    __table_args__ = {"schema": "shop"}

    Id = Column(Integer, primary_key=True)
    Tag = Column(String, nullable=False)


class Materials(Base):
    __tablename__ = "Materials"
    __table_args__ = {"schema": "shop"}

    Id = Column(Integer, primary_key=True)
    MaterialTypeId = Column(Integer, ForeignKey("shop.MaterialsTypes.Id"), nullable=False)
    Description = Column(String, nullable=False)


class Sellers(Base):
    __tablename__ = "Sellers"
    __table_args__ = {"schema": "shop"}

    Id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    State = Column(String, nullable=False)
    City = Column(String, nullable=False)


class Prices(Base):
    __tablename__ = "Prices"
    __table_args__ = {"schema": "shop"}

    Id = Column(Integer, primary_key=True)
    MaterialId = Column(Integer, ForeignKey("shop.Materials.Id"), nullable=False)
    SellerId = Column(Integer, ForeignKey("shop.Sellers.Id"), nullable=False)
    UnitPrice = Column(Float, nullable=False)
    MinForDiscount = Column(Integer, nullable=False)
    UnitPriceWithDiscount = Column(Float, nullable=False)


class Engineers(Base):
    __tablename__ = "Engineers"
    __table_args__ = {"schema": "planning"}

    Id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Title = Column(String, nullable=False)


class Projects(Base):
    __tablename__ = "Projects"
    __table_args__ = {"schema": "planning"}

    Id = Column(Integer, primary_key=True)
    EngineerId = Column(Integer, ForeignKey("planning.Engineers.Id"), nullable=False)
    Name = Column(String, nullable=False)
    AvailableBudget = Column(Float, nullable=False)


class Steps(Base):
    __tablename__ = "Steps"
    __table_args__ = {"schema": "planning"}

    Id = Column(Integer, primary_key=True)
    ProjectId = Column(Integer, ForeignKey("planning.Projects.Id"), nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    RealStartDate = Column(Date, nullable=False)
    RealEndDate = Column(Date, nullable=False)


class Budget(Base):
    __tablename__ = "Budget"
    __table_args__ = {"schema": "planning"}

    Id = Column(Integer, primary_key=True)
    StepId = Column(Integer, ForeignKey("planning.Steps.Id"), nullable=False)
    MaterialId = Column(Integer, ForeignKey("shop.Materials.Id"), nullable=False)
    Quantity = Column(Integer, nullable=False)
    AfterPlan = Column(Boolean, default=False)'''
