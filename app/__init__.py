from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"

    with app.app_context():
        from .models.user import User  # นำเข้าโมดูล User ที่นี่เพื่อหลีกเลี่ยง circular import

    from .routes import bp

    app.register_blueprint(bp)  # ลงทะเบียน Blueprint

    return app
