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
from app import db, mail
from flask_mail import Message
import logging

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
