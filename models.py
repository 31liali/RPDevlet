from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"

    # Kullanıcı Bilgileri
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        default="user"
    )

    # Para Sistemi
    money = db.Column(
        db.Integer,
        default=0
    )

    # Ehliyet
    license = db.Column(
        db.Boolean,
        default=False
    )

    license_type = db.Column(
        db.String(20),
        default="Yok"
    )

    # Ehliyete El Koyma
    license_blocked = db.Column(
        db.Boolean,
        default=False
    )

    # Kaç gün el konuldu
    # 0 = El konulmadı
    # -1 = Süresiz el koyma
    license_block_days = db.Column(
        db.Integer,
        default=0
    )

    # Tapu Sistemi
    garage_no = db.Column(
        db.String(50),
        default="Yok"
    )

    title_no = db.Column(
        db.String(50),
        default="Yok"
    )

    # Para Cezası
    fine_money = db.Column(
        db.Integer,
        default=0
    )

    # Cezalar
    fines = db.Column(
        db.Text,
        default=""
    )

    # İleride kullanabiliriz
    logs = db.Column(
        db.Text,
        default=""
    )