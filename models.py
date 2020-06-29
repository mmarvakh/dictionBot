from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Users(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_login = Column(String(length=64), nullable=False, index=True, unique=True)
    password_hash = Column(String(length=128), nullable=True)
    chosen_time = Column(Time, nullable=True)
    chosen_days = Column(String(length=100), nullable=True)
    chosen_plan = Column(Integer, ForeignKey('plans.id'), default=None)
    current_day = Column(Integer, nullable=True, default=1)

class Exercises(base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=100), nullable=False)
    exercise_day = Column(Integer, nullable=False)
    exercise_text = Column(Text, nullable=False)
    plan_number = Column(Integer, ForeignKey('plans.id'), default=None)

class Plans(base):
    __tablename__ = 'plans'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    number = Column(Integer, nullable=False)
    exercises = relationship('Exercises', backref='plan', lazy='dynamic')
    users = relationship('Users', backref='plan_user', lazy='dynamic')