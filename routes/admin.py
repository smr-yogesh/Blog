from flask import render_template, request, redirect, url_for, Blueprint, flash, session
from utils.db import db
from datetime import datetime
from model.post import blogpost

admin_B = Blueprint('admin_B', __name__)

@admin_B.route('/admin')
def admin():
    session["track"] = "admin_B.admin"
    if "user" in session:
        uid = session["user_id"]
        posts = blogpost.query.filter_by(user_id=uid).all() 
        return render_template('admin.html', posts=posts)
    flash("! Please login first !")
    return redirect(url_for('B_user.register', mode='login'))

@admin_B.route('/addpost')
def a_p():
    if "user" in session:
        return render_template('addpost.html')
    session["track"] = "admin_B.a_p"
    flash("! Please login first !")
    return redirect(url_for('B_user.register', mode='login'))

@admin_B.route('/ap', methods=['POST'])
def ap():
    title = request.form['title']
    author = request.form['author']
    content = request.form['content']
    uid = session["user_id"]

    post = blogpost(title=title, author=author, content=content, date_posted=datetime.now(), updated=None, user_id = uid)

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('admin_B.admin'))

@admin_B.route('/edit/', methods=['POST','GET'])
def edit():
    post_id = request.form['edit_id']
    post_to_edit = blogpost.query.filter_by(id=post_id).one()
    session["post_id"] = post_id
    return render_template ('updatepost.html', post=post_to_edit)

@admin_B.route('/update', methods=['POST'])
def update():
    post_id = request.form['edit_id']
    title = request.form['title']
    author = request.form['author']
    content = request.form['content']
    post = blogpost.query.filter_by(id=post_id).one()
    post.title = title
    post.author = author
    post.content = content
    post.updated = datetime.now()
    db.session.commit()
    flash("Edited successfully!!","message-success")
    return redirect(url_for('admin_B.admin'))

@admin_B.route('/delete', methods=['POST'])
def delete():
    id  = request.form['del_id']
    post_to_del = blogpost.query.get_or_404(id)
    try:
        db.session.delete(post_to_del)
        db.session.commit()
        flash("Deleted successfully!!","message-success")
    except:
        flash("something went wrong!!")
    return redirect(url_for('admin_B.admin'))

