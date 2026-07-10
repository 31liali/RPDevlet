from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from app import db, bcrypt
from models import User

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first():
            flash("Bu kullanıcı adı zaten kullanılıyor.")
            return redirect(url_for("auth.register"))

        hashed = bcrypt.generate_password_hash(password).decode("utf-8")

        user = User(
            username=username,
            password=hashed,
            money=0,
            license=False,
            license_type="Yok",
            garage_no="Yok",
            title_no="Yok",
            role="user",
            fines="",
            logs="Hesap oluşturuldu."
        )

        db.session.add(user)
        db.session.commit()

        flash("Hesap başarıyla oluşturuldu.")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect("/home")

        flash("Kullanıcı adı veya şifre yanlış.")

    return render_template("login.html")


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))