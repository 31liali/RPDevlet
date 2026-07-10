import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Flask
    SECRET_KEY = "BURAYA_DAHA_SONRA_GUCLU_BIR_ANAHTAR_GELECEK"

    # SQLite Veritabanı
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False