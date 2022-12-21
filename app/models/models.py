from app import db


class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(1000))