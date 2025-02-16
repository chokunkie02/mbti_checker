
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)  # โหลดการตั้งค่าทั้งหมดจาก Config class

    # เริ่มต้นส่วนขยาย
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # ลงทะเบียน Blueprint
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    # สร้างตารางในฐานข้อมูล
    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    return app