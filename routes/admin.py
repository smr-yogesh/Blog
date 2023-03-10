from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash, session
from utils.db import db
from datetime import datetime
from model.post import blogpost

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def add():
    if "user" in session:
        user = session["user"]
        uid = session["user_id"]
        posts = blogpost.query.filter_by(user_id=uid).all() 
        return render_template('admin.html', posts=posts)
    return render_template('sign_in.html', response = "! Please login first !")

@admin.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']
    uid = session["user_id"]

    post = blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now(), user_id = uid)

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('B_user.index'))

@admin.route('/delete', methods=['POST'])
def delete():
    id  = request.form['del_id']
    post_to_del = blogpost.query.get_or_404(id)
    try:
        db.session.delete(post_to_del)
        db.session.commit()
        flash("Deleted successfully!!")
    except:
        flash("something went wrong!!")
    return redirect(url_for('admin.add'))