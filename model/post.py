from utils.db import db
from datetime import datetime


class blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer)