from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User
from app import db, mail
from flask_mail import Message

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


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("main.home"))
        else:
            flash("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    return render_template("login.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("รหัสผ่านไม่ตรงกัน")
            return redirect(url_for("main.register"))

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("สมัครสมาชิกสำเร็จแล้ว กรุณาเข้าสู่ระบบ")
        return redirect(url_for("main.login"))

    return render_template("register.html")


@bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form["email"]
        user = User.query.filter_by(email=email).first()
        if user:
            token = user.get_reset_password_token()
            send_reset_email(user, token)
            flash("ลิงก์รีเซ็ตรหัสผ่านถูกส่งไปยังอีเมลของคุณแล้ว")
            return redirect(url_for("main.login"))
        else:
            flash("ไม่พบผู้ใช้งานที่มีอีเมลนี้")
    return render_template("forgot-password.html")


def send_reset_email(user, token):
    msg = Message(
        "รีเซ็ตรหัสผ่าน", sender="noreply@mbti_checker.com", recipients=[user.email]
    )
    msg.body = f"""เพื่อรีเซ็ตรหัสผ่านของคุณ กรุณาคลิกที่ลิงก์ด้านล่าง:
{url_for('main.reset_password', token=token, _external=True)}

หากคุณไม่ได้ทำการร้องขอการรีเซ็ตรหัสผ่าน กรุณาละเว้นอีเมลนี้
"""
    mail.send(msg)


@bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for("main.home"))
    if request.method == "POST":
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if password != confirm_password:
            flash("รหัสผ่านไม่ตรงกัน")
            return redirect(url_for("main.reset_password", token=token))
        user.set_password(password)
        db.session.commit()
        flash("รหัสผ่านของคุณถูกรีเซ็ตเรียบร้อยแล้ว")
        return redirect(url_for("main.login"))
    return render_template("reset-password.html", token=token)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))


@bp.route("/save_mbti", methods=["POST"])
def save_mbti():
    if current_user.is_authenticated:
        # Save MBTI result to the database for logged-in users
        mbti_result = request.form["mbti_result"]
        # Save the result to the user's profile or another table
        # Example: current_user.mbti_result = mbti_result
        db.session.commit()
    else:
        # Save MBTI result to the session for temporary storage
        session["mbti_result"] = request.form["mbti_result"]
    return redirect(url_for("main.result"))
