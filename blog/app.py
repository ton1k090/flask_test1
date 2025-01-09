from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .extension import db, login_manager
from .models import User
from .user.views import user
from .reports.views import report
from .auth.views import auth
from .index.views import index


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'e*g2wrmibud-s&qhvvj+gaqpmo9zk-a$o%x%836e-c9j%c9)44'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    register_extensions(app)
    from .models import User

    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):

    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(auth)
    app.register_blueprint(index)
