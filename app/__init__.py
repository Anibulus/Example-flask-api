from app.config import Config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .auth import auth
from .models import UserModel

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)


def create_app():
    app = Flask(__name__) #El nobre de la app se colocara como main de esta manera
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    login_manager.init_app(app)

    app.register_blueprint(auth)
    return app