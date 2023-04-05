from flask import Flask, request, jsonify, session, flash
import jwt
from services import users as UserService
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Error': 'Token is missing.'}), 401

        try:
            data = jwt.decode(token, '1234567890', algorithms=['HS256', ])
        except jwt.InvalidTokenError:
            return jsonify({'Message': 'Invalid token.'}), 403
        return func(*args, **kwargs)
    return decorated


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = UserService.login(data)
    return jsonify(result)


@app.route("/index")
@token_required
def index():
    service = UserService
    result = service.all()
    return jsonify(result)


@app.route('/create-user', methods=['POST'])
def create():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
        result = UserService.create(data)
        return result

