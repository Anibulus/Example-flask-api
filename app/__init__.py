from app.config import Config
from flask import Flask
from flask_bootstrap import Bootstrap
from .auth import auth

def create_app():
    app = Flask(__name__) #El nobre de la app se colocara como main de esta manera
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    app.register_blueprint(auth)
    return app