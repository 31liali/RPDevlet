from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from app import db
from models import User

admin = Blueprint("admin", __name__)


# =====================================
# ADMIN KONTROLÜ
# =====================================

def is_admin():

    if not current_user.is_authenticated:
        return False

    return (
        current_user.username == "A.B"
        and current_user.role == "admin"
    )


# =====================================
# ADMIN PANELİ
# =====================================

@admin.route("/admin")
@login_required
def admin_panel():

    if not is_admin():

        flash("Bu sayfaya erişim yetkiniz yok.")

        return redirect("/home")

    return render_template("admin.html")


# =====================================
# KULLANICI ARA
# =====================================

@admin.route("/admin/search")
@login_required
def search():

    if not is_admin():

        flash("Yetkiniz bulunmuyor.")

        return redirect("/home")

    username = request.args.get("username")

    if not username:

        flash("Kullanıcı adı giriniz.")

        return redirect("/admin")

    user = User.query.filter_by(
        username=username
    ).first()

    if not user:

        flash("Kullanıcı bulunamadı.")

        return redirect("/admin")

    return redirect(f"/admin/user/{user.id}")


# =====================================
# KULLANICI DETAY
# =====================================

@admin.route("/admin/user/<int:user_id>")
@login_required
def user_info(user_id):

    if not is_admin():

        flash("Yetkiniz bulunmuyor.")

        return redirect("/home")

    target = User.query.get_or_404(user_id)

    return render_template(
        "admin_user.html",
        target=target
    )


# =====================================
# PARA VER
# =====================================

@admin.route("/admin/money", methods=["POST"])
@login_required
def give_money():

    if not is_admin():

        flash("Yetkiniz bulunmuyor.")

        return redirect("/home")

    username = request.form["username"]

    amount = int(
        request.form["amount"]
    )

    user = User.query.filter_by(
        username=username
    ).first()

    if not user:

        flash("Kullanıcı bulunamadı.")

        return redirect("/admin")

    user.money += amount

    db.session.commit()

    flash("Para başarıyla verildi.")

    return redirect("/admin")
# =====================================
# EHLİYET VER
# =====================================

@admin.route("/admin/license", methods=["POST"])
@login_required
def give_license():

    if not is_admin():
        flash("Yetkiniz bulunmuyor.")
        return redirect("/home")

    username = request.form["username"]
    license_type = request.form["license"]

    user = User.query.filter_by(
        username=username
    ).first()

    if not user:
        flash("Kullanıcı bulunamadı.")
        return redirect("/admin")

    user.license = True
    user.license_type = license_type

    db.session.commit()

    flash("Ehliyet başarıyla verildi.")

    return redirect("/admin")


# =====================================
# TAPU VER
# =====================================

@admin.route("/admin/title", methods=["POST"])
@login_required
def give_title():

    if not is_admin():
        flash("Yetkiniz bulunmuyor.")
        return redirect("/home")

    username = request.form["username"]

    garage = request.form["garage"]

    title = request.form["title"]

    user = User.query.filter_by(
        username=username
    ).first()

    if not user:
        flash("Kullanıcı bulunamadı.")
        return redirect("/admin")

    user.garage_no = garage
    user.title_no = title

    db.session.commit()

    flash("Tapu başarıyla verildi.")

    return redirect("/admin")


# =====================================
# CEZA KES
# =====================================

@admin.route("/admin/fine", methods=["POST"])
@login_required
def give_fine():

    if not is_admin():
        flash("Yetkiniz bulunmuyor.")
        return redirect("/home")

    username = request.form["username"]

    fine_type = request.form["type"]

    user = User.query.filter_by(
        username=username
    ).first()

    if not user:
        flash("Kullanıcı bulunamadı.")
        return redirect("/admin")

    # Süresiz Ehliyet El Koyma
    if fine_type == "Ehliyete El Koyma":

        user.license_blocked = True
        user.license_block_days = -1

    # Süreli El Koyma
    elif fine_type == "Ehliyete Süreli El Koyma":

        days = int(request.form["amount"])

        user.license_blocked = True
        user.license_block_days = days

    # Para Cezası
    elif fine_type == "Para Cezası":

        amount = int(request.form["amount"])

        user.fine_money += amount

    db.session.commit()

    flash("Ceza başarıyla uygulandı.")

    return redirect("/admin")
# =====================================
# EHLİYET CEZASINI KALDIR
# =====================================

@admin.route("/admin/remove_license_block", methods=["POST"])
@login_required
def remove_license_block():

    if not is_admin():
        flash("Yetkiniz bulunmuyor.")
        return redirect("/home")

    username = request.form["username"]

    user = User.query.filter_by(
        username=username
    ).first()

    if not user:
        flash("Kullanıcı bulunamadı.")
        return redirect("/admin")

    user.license_blocked = False
    user.license_block_days = 0

    db.session.commit()

    flash("Ehliyet üzerindeki ceza kaldırıldı.")

    return redirect("/admin")


# =====================================
# PARA CEZASINI SIFIRLA
# =====================================

@admin.route("/admin/reset_fine", methods=["POST"])
@login_required
def reset_fine():

    if not is_admin():
        flash("Yetkiniz bulunmuyor.")
        return redirect("/home")

    username = request.form["username"]

    user = User.query.filter_by(
        username=username
    ).first()

    if not user:
        flash("Kullanıcı bulunamadı.")
        return redirect("/admin")

    user.fine_money = 0
    user.fines = ""

    db.session.commit()

    flash("Para cezası sıfırlandı.")

    return redirect("/admin")