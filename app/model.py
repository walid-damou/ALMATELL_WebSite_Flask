from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    num = db.Column(db.String(30), nullable=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sujet = db.Column(db.String(30), nullable=False)
    mdate = db.Column(db.String(30), nullable=False)
    message = db.Column(db.Text, nullable=False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
