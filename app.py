from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Blueprint'ler
from routes.auth import auth
from routes.admin import admin
from routes.user import user

app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(user)


@app.route("/")
def index():
    return "<script>window.location='/login';</script>"


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )