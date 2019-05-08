from flask import Flask, session, request, flash, url_for, redirect, render_template, abort ,g
from flask_restplus import Api
from flask_login import LoginManager, login_user , logout_user , current_user , login_required

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    from config import Config
    app.config.from_object(Config)
    db.init_app(app)



    @app.route('/login')
    def login():
        return "login"

    @app.route('/register')
    def register():
        return "register"

    from .apis.tweets import api as tweets
    from .apis.users import api as users
    api = Api()
    api.add_namespace(tweets)
    api.add_namespace(users)
    api.init_app(app)

    app.config['ERROR_404_HELP'] = False
    return app
