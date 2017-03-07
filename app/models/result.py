from flask import current_app

from .. import db

class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer)
    language = db.Column(db.String(8),default='EN')
    item = db.Column(db.String(255))
    text = db.Column(db.Text)
