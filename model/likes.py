from utils.db import db
from datetime import datetime


class likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    like_amt = db.Column(db.Integer)
