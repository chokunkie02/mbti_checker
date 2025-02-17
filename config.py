import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "your-secret-key-here"  # ควรเปลี่ยนเป็นค่าที่ปลอดภัยในการใช้งานจริง
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
