from flask import current_app
from . import Question
from sqlalchemy.sql import func

from .. import db


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    questionId = db.Column(db.Integer, db.ForeignKey(Question.id))
    altQuestionId = db.Column(db.Integer, db.ForeignKey(Question.id))
    answerValue = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime, server_default=func.now())
    source = db.Column(db.Integer)

class AnswerMeta(db.Model):
    __tablename__ = 'answer_meta'
    id = db.Column(db.Integer, primary_key=True)
    answerId = db.Column(db.Integer, db.ForeignKey(Answer.id))
    key = db.Column(db.String(255))
    value = db.Column(db.String(255))
