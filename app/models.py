from datetime import datetime
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.event import listen
import uuid

def generate_key(mapper, connect, target):
    target.generate_key()

class Tweet(db.Model):
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = db.relationship("User", back_populates="tweets")

    def __repr__(self):
        return f"<Tweet #{self.id}>"

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column('password' , db.String(20))
    email = db.Column('email',db.String(50))
    key = db.Column(db.String(150))
    tweets = db.relationship('Tweet', back_populates="user")

    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email

    def generate_key(self):
        if not self.key:
            self.key = str(uuid.uuid4())
        return self.key

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"<User {self.username}>"

listen(User, 'before_insert', generate_key)
