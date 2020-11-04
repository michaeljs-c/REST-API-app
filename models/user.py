import sqlite3
from db import db

class UserModel(db.Model):
    #These declarations are soley for SQLAlchemy. They need to match the variables in __init__
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
#defining as a class mathod, using 'cls' below to call the class method
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() #SELECT * FROM users WHERE username=username LIMIT 1

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
