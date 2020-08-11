from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import models, views

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DMessages.db'
db = SQLAlchemy(app)


