from flask import current_app

from .. import db


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

class QuestionText(db.Model):
    __tablename__ = 'question_text'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(Question.id))
    language = db.Column(db.String(8),default='EN')
    text = db.Column(db.UnicodeText)
