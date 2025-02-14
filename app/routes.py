from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app import db

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/quiz")
def quiz():
    return render_template("quiz.html")


@bp.route("/result")
def result():
    return render_template("result.html")


@bp.route("/characters")
def characters():
    return render_template("characters.html")


@bp.route("/relationships")
def relationships():
    return render_template("relationships.html")


@bp.route("/history")
def history():
    return render_template("history.html")


@bp.route("/mbti/<type>")
def mbti_type(type):
    return render_template("mbti_type.html", type=type)


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/careers")
def careers():
    return render_template("careers.html")


@bp.route("/contact")
def contact():
    return render_template("contact.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("main.home"))
        else:
            flash("อีเมลหรือรหัสผ่านไม่ถูกต้อง")
    return render_template("login.html")


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))
