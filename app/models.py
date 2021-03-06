# from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5
from app import db

#the tables of sql and related caculations are wirtten here

# User table
class User(UserMixin,db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    Is_adm = db.Column(db.Integer)
    mark = db.Column(db.Integer)
    answer = db.relationship('answer', backref='author', lazy='dynamic')
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_id(self):
        return self.id

    def get_user_name(self):
        return self.username
    
    def if_adm(self):
        return self.Is_adm
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    
# question table
class questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))
    stand_answer = db.Column(db.String(500))
    mark = db.Column(db.Integer)
    tag = db.Column(db.String(20))
    type = db.Column(db.String(20))
    answer = db.relationship('answer', backref='question', lazy='dynamic')

    def __repr__(self):
        return '<"questions": {},'.format(self.content)+'"tag": {}'.format(self.tag)+">"

    def get_id(self):
        return self.id
    
    def get_content(self):
        return self.content
    
    def get_set(self):
        return self.tag
    def get_mark(self):
        return self.mark
    def get_answer(self):
        return self.stand_answer


# answer table
class answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id=db.Column(db.Integer, db.ForeignKey('questions.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String(500))
    mark = db.Column(db.Integer, default=-1)
    def __repr__(self):
        return '<answer {}>'.format(self.content)
       