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
