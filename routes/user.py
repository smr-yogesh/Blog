from flask import Flask, render_template, request, redirect, url_for, Blueprint, session
from werkzeug.security import check_password_hash
from utils.db import db
from model.user import user as user_data
from model.post import blogpost

B_user = Blueprint('B_user', __name__)

@B_user.route('/')
def index():
    db.create_all()
    if "user" in session:
        user = session["user"]
    posts = blogpost.query.order_by(blogpost.date_posted.desc()).all()

    return render_template('index.html', posts=posts)

@B_user.route('/signup', methods=['POST', 'GET'])
def signup():
    #data = request.form.get()
    email = request.form['email']
    password = request.form['password']

    users = user_data(email,password)

    db.session.add(users)
    db.session.commit()

    return redirect(url_for('B_user.index'))

@B_user.route('/register', methods = ['POST','GET'])
def register():
    return render_template('sign_in.html')


@B_user.route('/signin', methods = ['POST','GET'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = user_data.query.filter_by(email=email).first()
        if check_password_hash(user.pswd, password):
            session["user"] = email
            session["user_id"] = user.id
            return render_template('sign_in.html', response = "login successfull")
        else :
            return render_template('sign_in.html', response = "invalid password")

@B_user.route('/post/<int:post_id>')
def post(post_id):
    post = blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@B_user.route('/about')
def about():
    return render_template('about.html')