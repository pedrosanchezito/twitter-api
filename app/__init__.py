from flask import Flask, request, render_template
from flask_restplus import Api
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    from config import Config
    app.config.from_object(Config)
    db.init_app(app)

    @app.route('/hello')
    def hello():
        return "Goodbye World!"

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @app.route('/register' , methods=['GET','POST'])
    def register():
        if request.method == 'GET':
            return render_template('register.html')
        user = User(request.form['username'] , request.form['password'],request.form['email'])
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered')
        return redirect(url_for('login'))

    @app.route('/login',methods=['GET','POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        return redirect(url_for('index'))

    from .apis.tweets import api as tweets
    api = Api()
    api.add_namespace(tweets)
    api.init_app(app)

    app.config['ERROR_404_HELP'] = False
    return app
