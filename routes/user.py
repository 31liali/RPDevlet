from flask import Blueprint, render_template
from flask_login import login_required, current_user

user = Blueprint("user", __name__)


# Ana Sayfa
@user.route("/home")
@login_required
def home():

    return render_template(
        "home.html",
        user=current_user
    )


# Profil
@user.route("/profile")
@login_required
def profile():

    return render_template(
        "profile.html",
        user=current_user
    )


# Para
@user.route("/money")
@login_required
def money():

    return render_template(
        "money.html",
        money=current_user.money
    )


# Ehliyet
@user.route("/license")
@login_required
def license_page():

    return render_template(
        "license.html",
        license=current_user.license,
        license_type=current_user.license_type
    )


# Tapu
@user.route("/title")
@login_required
def title():

    return render_template(
        "title.html",
        garage=current_user.garage_no,
        title=current_user.title_no
    )


# Cezalar
@user.route("/fines")
@login_required
def fines():

    fines = []

    if current_user.fines:
        fines = current_user.fines.split("\n")

    return render_template(
        "fines.html",
        fines=fines
    )


# İşlem Geçmişi
@user.route("/logs")
@login_required
def logs():

    logs = []

    if current_user.logs:
        logs = current_user.logs.split("\n")

    return render_template(
        "logs.html",
        logs=logs
    )