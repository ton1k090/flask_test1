from flask_login import UserMixin
from .app import db


class User(db.Model, UserMixin):
    '''Создать таблицу пользователей'''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    password = db.Column(db.String(250))