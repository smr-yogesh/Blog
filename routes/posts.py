from flask import render_template, request, redirect, url_for, Blueprint, flash, session
from utils.db import db
from datetime import datetime
from model.post import blogpost

posts_B = Blueprint('posts_B', __name__)

@posts_B.route('/addpost')
def a_p():
    if "user" in session:
        return render_template('addpost.html')
    session["track"] = "posts_B.a_p"
    flash("! Please login first !")
    return redirect(url_for('B_user.register', mode='login'))

@posts_B.route('/ap', methods=['POST'])
def ap():
    title = request.form['title']
    author = request.form['author']
    content = request.form['ckeditor']
    uid = session["user_id"]

    post = blogpost(title=title, author=author, content=content, date_posted=datetime.now(), updated=None, user_id = uid)

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('admin_B.admin'))

@posts_B.route('/edit/', methods=['POST','GET'])
def edit():
    post_id = request.form['edit_id']
    post_to_edit = blogpost.query.filter_by(id=post_id).one()
    return render_template ('updatepost.html', post=post_to_edit)

@posts_B.route('/update', methods=['POST'])
def update():
    post_id = request.form['edit_id']
    title = request.form['title']
    author = request.form['author']
    content = request.form['content']
    word = content.split()
  #  if word[0] == "[Edited]":
  #      pass
  #  else:
  #      content = "[Edited]&emsp;" + content

    post = blogpost.query.filter_by(id=post_id).one()
    post.title = title
    post.author = author
    post.content = content
    post.updated = datetime.now()
    db.session.commit()
    flash("Edited successfully!!","message-success")
    return redirect(url_for('admin_B.admin'))

@posts_B.route('/delete', methods=['POST'])
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