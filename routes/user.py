from flask import render_template, request, redirect, url_for, Blueprint, session,flash
from werkzeug.security import check_password_hash
from utils.db import db
from model.user import user as user_data
from model.post import blogpost

B_user = Blueprint('B_user', __name__)

def users_count():
    total = 0
    userss = (user_data.query.order_by(user_data.user_id.desc())).all()
    for each in userss:
        if each.user_id > total:
            total = each.user_id

    return total


@B_user.route('/')
def index():
    db.create_all()
    if "user" in session:
        user_i = session["user_id"]
        posts = blogpost.query.filter_by(user_id=user_i).all() 
        return render_template('index.html', posts=posts)
    posts = blogpost.query.all() 
    return render_template('index.html', posts=posts)

@B_user.route('/register', methods = ['POST','GET'])
def register():
    if "user" in session:
        return redirect(url_for('B_user.index'))
    return render_template('sign_in.html')

@B_user.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        
        user_id = 1 + users_count()
        users = user_data(email,password,user_id,name)

        db.session.add(users)
        db.session.commit()

        return redirect(url_for('B_user.signin'))
    
    return redirect(url_for('B_user.register', mode='signup'))

@B_user.route('/signin', methods = ['POST','GET'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try :
            user = user_data.query.filter_by(email=email).first()
            if (check_password_hash(user.pswd, password)):
                session["user"] = user.name
                session["user_id"] = user.user_id
                if "track" in session :
                    return redirect(url_for(session["track"]))
                return redirect(url_for('B_user.index'))
            else :
                flash("Invalid credentials ")
                return redirect(url_for('B_user.register', mode='login'))
        except:
            flash("Invalid credentials ")
            return redirect(url_for('B_user.register', mode='login'))
        
    return redirect(url_for('B_user.register', mode='login'))

@B_user.route('/logout')
def logout():
    session.pop("user", None)
    session.pop("user_id", None)
    session.pop("message", None)
    session.pop("track", None)
    return redirect(url_for('B_user.index'))

@B_user.route('/post/<int:post_id>')
def post(post_id):
    post = blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@B_user.route('/contact')
def contact():
    return render_template('contact.html')

@B_user.route('/pop')
def pop():
    session.pop("post_title", None)
    session.pop("post_author", None)
    session.pop("post_content", None)
    session.pop("post_id", None)
    return redirect(url_for('admin_B.admin')) 