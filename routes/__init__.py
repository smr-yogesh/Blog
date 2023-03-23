from flask import Flask
from utils.db import db
from flask_ckeditor import CKEditor

app = Flask(__name__)


app = Flask(__name__,static_url_path='', static_folder=r'../static')

app.template_folder = '../templates'
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

app.config['CKEDITOR_PKG_TYPE'] = 'standard'
ckeditor = CKEditor(app)

db.init_app(app)