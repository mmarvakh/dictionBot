from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from config import ENGINE

engine = ENGINE

db = declarative_base()


class Users(db):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_login = Column(String(length=64), nullable=False, index=True, unique=True)
    password_hash = Column(String(length=128), nullable=True)

class Plan_1(db):
    __tablename__ = 'plan_1'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=100), nullable=False)
    exercise_day = Column(Integer, nullable=False)
    exercise_text = Column(Text, nullable=False)
    plan = Column(String(length=30), nullable=False)

class Plan_2(db):
    __tablename__ = 'plan_2'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=100), nullable=False)
    exercise_day = Column(Integer, nullable=False)
    exercise_text = Column(Text, nullable=False)
    plan = Column(String(length=30), nullable=False)

class Plan_3(db):
    __tablename__ = 'plan_3'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=100), nullable=False)
    exercise_day = Column(Integer, nullable=False)
    exercise_text = Column(Text, nullable=False)
    plan = Column(String(length=30), nullable=False)

class AboutDiction(db):
    __tablename__ = 'about_diction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=100), nullable=False)
    text = Column(Text, nullable=False)