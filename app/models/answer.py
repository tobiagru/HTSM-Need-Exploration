from flask import current_app
from . import Question
from sqlalchemy.sql import func

from .. import db


class AnswerMeta(db.Model):
    __tablename__ = 'answer_meta'
    id = db.Column(db.Integer, primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey(Answer.id))
    key = db.Column(db.String(255))
    value = db.Column(db.String(255))

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(Question.id))
    alt_question = db.Column(db.Integer, db.ForeignKey(Question.id))
    answer = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime, server_default=func.now())
    source = db.Column(db.Integer)
