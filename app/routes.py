from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    session,
    send_from_directory,
)
from app import db
from app.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required

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

@bp.route("/about")
def about():
    return render_template("about.html")

@bp.route("/contact")
def contact():
    return render_template("contact.html")

@bp.route("/save_mbti", methods=["POST"])
def save_mbti():
    mbti_result = request.form["mbti_result"]
    session["mbti_result"] = mbti_result
    return redirect(url_for("main.result"))

@bp.route("/favicon.ico")
def favicon():
    return send_from_directory("static/mbti", "ISFP.ico")

@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(display_name=form.display_name.data, username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("main.login"))
        login_user(user)
        return redirect(url_for("main.home"))
    return render_template("login.html", form=form)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))
