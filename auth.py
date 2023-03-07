import jwt 
from functools import wraps
from flask import Flask, request, jsonify
from routes import app
from model.user import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers['x-access-token']
        #token = request.args.get('token')  to pass via url
        if not token:
            return jsonify ({'message':'Token is required!'}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"],algorithms='HS256')
            user = User.query.filter_by(email=data['user']).first()
        except:
            return jsonify({'message':'Invalid token'}), 401
        return f(user,*args, **kwargs)
    return decorated
