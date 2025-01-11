from os import getenv, path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from json import load


from .extension import db, login_manager, migrate, csrf
from .models import User
from .user.views import user
from .reports.views import report
from .auth.views import auth
from .index.views import index


CONFIG_PATH = getenv("CONFIG_PATH", path.join("../dev_config.json"))


def create_app():
    app = Flask(__name__)
    app.config.from_file(CONFIG_PATH, load)

    register_extensions(app)
    from .models import User

    register_blueprints(app)
    return app


def register_extensions(app):
    '''Расширение Фласк'''

    db.init_app(app)
    csrf.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    migrate.init_app(app, db, compare_type=True)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):
    '''Зарегистрировать Блупринты ( приложения )'''
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(auth)
    app.register_blueprint(index)
