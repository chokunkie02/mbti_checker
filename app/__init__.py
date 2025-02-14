from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import Config

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"

    with app.app_context():
        from .models.user import User  # นำเข้าโมดูล User ที่นี่เพื่อหลีกเลี่ยง circular import

    @login_manager.user_loader
    def load_user(user_id):
        from .models.user import User  # นำเข้าโมดูล User ที่นี่เพื่อหลีกเลี่ยง circular import

        return User.query.get(int(user_id))

    from app.routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app
