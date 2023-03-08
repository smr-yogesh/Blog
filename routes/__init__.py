from flask import Flask
from utils.db import db
import os

app = Flask(__name__,static_url_path='', static_folder=r'../static')

app.template_folder = '../templates'
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.app_context()
db.init_app(app)