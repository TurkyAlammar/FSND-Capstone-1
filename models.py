import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

database_path = 'postgres://timjcpwcrvoyjm:9c9893f05df1fe964295d8827cb83e01c772edf215457c6f65e2b9bf789e373c@ec2-3-219-111-26.compute-1.amazonaws.com:5432/dcosc463uh5uk3'

db = SQLAlchemy()


def setup_db(app, database_path = database_path ):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

    
class Movies (db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(db.DateTime, nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
         'id': self.id,
         'title': self.title,
         'release date': self.release_date,
        }
    '''
    Actors

    '''


class Actors (db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String(3))
    gender = Column(String(6))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
         'id': self.id,
         'name': self.name,
         'age': self.age,
         'gender': self.gender
        }

