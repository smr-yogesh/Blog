from utils.db import db
from werkzeug.security import generate_password_hash
from datetime import datetime

class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(20), unique=True)
    pswd = db.Column(db.String(255))
    user_id = db.Column(db.Integer)

    def __init__(self,email,pswd,user_id):
       self.email= email
       self.pswd = generate_password_hash(pswd, method='sha256')
       self.user_id = user_id