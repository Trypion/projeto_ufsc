from functools import wraps
from app import app
from flask import request, jsonify
import jwt


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'token is missing', 'data': []}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = data['user_id']
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
        return f(user, *args, **kwargs)
    return decorated