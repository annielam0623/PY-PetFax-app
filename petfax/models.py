from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

class Fact(db.Model):
    __tablename__ = "facts"

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(250))
    fact = db.Column(db.Text)